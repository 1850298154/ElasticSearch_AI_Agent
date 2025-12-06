
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from annoy import AnnoyIndex


class ElasticsearchSearch:
    def __init__(self, url):
        self.es = Elasticsearch([url], max_retries=10)
        self.index_name = datetime.now().strftime('%Y%m%d-%H%M%S') + "_test_es_search"

    def create_index(self, mapping):
        self.es.indices.create(index=self.index_name, body=mapping)

    def create_index_usually_used(self):
        mapping={
            "mappings": {
                "properties": {
                    "content": {
                        "type": "text",
                        "analyzer": "custom_lowercase_analyzer"
                    }
                }
            },
            "settings": {
                "analysis": {
                    "analyzer": {
                        "custom_lowercase_analyzer": {
                            "type": "custom",
                            "tokenizer": "standard",
                            "filter": ["lowercase"]
                        }
                    }
                }
            }
        }
        self.create_index(mapping)

    def insert_data(self, doc_id, doc_body):
        self.es.index(index=self.index_name, id=doc_id, body=doc_body)

    def refresh_index(self):
        self.es.indices.refresh(index=self.index_name)

    def build_vector_index(self, vector_size, metric="angular", num_trees=10):
        vector_index = AnnoyIndex(vector_size, metric=metric)
        for doc_id in range(1, 3):
            vector = self.es.get(index=self.index_name, id=doc_id)["_source"]["vector"]
            vector_index.add_item(doc_id, vector)
        vector_index.build(num_trees)
        return vector_index

    def keyword_search(self, keywords, fields=["title", "content"]):
        search_body_single = {
            "query": {
                "match": {
                    "content": keywords,
                }
            }
        }
        result = self.es.search(index=self.index_name, body=search_body_single)
        return result

    def structured_search(self, query):
        s = Search(using=self.es, index=self.index_name).query(Q("match", content=query))
        result = s.execute()
        return result

    def vector_search(self, vector_index, query_vector, n=5):
        similar_docs = vector_index.get_nns_by_vector(query_vector, n=n)
        docs_info = [self.es.get(index=self.index_name, id=doc_id)["_source"] for doc_id in similar_docs]
        return docs_info

    def vector_search_on_keywords(self, keyword_result, vector_index):
        keyword_result_ids = [int(hit["_id"]) for hit in keyword_result["hits"]["hits"]]
        vector_index_filtered = AnnoyIndex(len(vector_index.get_item_vector(0)), metric="angular")
        for doc_id in keyword_result_ids:
            vector = self.es.get(index=self.index_name, id=doc_id)["_source"]["vector"]
            vector_index_filtered.add_item(doc_id, vector)
        vector_index_filtered.build(10)
        similar_docs = vector_index_filtered.get_nns_by_vector(vector_index.get_item_vector(0), n=len(keyword_result_ids))
        docs_info = [self.es.get(index=self.index_name, id=doc_id)["_source"] for doc_id in similar_docs]
        return docs_info

    def comprehensive_search(self, query, query_vector):
        keyword_result = self.keyword_search(query)
        structured_result = self.structured_search(query)
        
        vector_index = self.build_vector_index(len(query_vector))
        vector_result = self.vector_search(vector_index, query_vector)
        vector_result_filtered = self.vector_search_on_keywords(keyword_result, vector_index)

        return {
            "Keyword Search Result": keyword_result,
            "Structured Search Result": structured_result.hits,
            "Vector Search Result": vector_result,
            "Vector Search Result on Keyword Search": vector_result_filtered
        }


query = "programming"
query_vector = [0.15, 0.25, 0.35]
# es_search = ElasticsearchSearch("http://<your_es_account>:<your_es_password>@<your_es_server_ip>:6030")
es_search = ElasticsearchSearch("http://elastic:xxx@localhost:9200")
es_search.create_index_usually_used()
es_search.insert_data(doc_id=1, doc_body={
    "title": "Elasticsearch is powerful",
    "content": "Elasticsearch is a distributed search and analytics engine.",
    "vector": [0.1, 0.2, 0.3]
})
es_search.insert_data(doc_id=2, doc_body={
    "title": "Python a programming",
    "content": "Python is a versatile programming language.",
    "vector": [0.4, 0.5, 0.6]
})
es_search.refresh_index()
result = es_search.comprehensive_search(query, query_vector)
print("Comprehensive Search Result:", result)






"""
docker run -d --name es -e "ES_JAVA_OPTS=-Xms512m -Xmx4024m" -e "discovery.type=single-node" -e "xpack.security.enabled=false" -e "xpack.security.transport.ssl.enabled=false" -e "ELASTIC_PASSWORD=xxx" -v es-data4:/home/xxx/es4/data -v es-plugins4:/home/xxx/es4/plugin --privileged -p 9200:9200 -p 9300:9300  elasticsearch:8.16.1


D:\zyt\git_ln\ElasticSearch_AI_Agent> cmd /C "c:\Python313\python.exe c:\Users\zooos\.vscode\extensions\ms-python.debugpy-2025.16.0-win32-x64\bundled\libs\debugpy\launcher 25623 -- D:\zyt\git_ln\ElasticSearch_AI_Agent\test.py "
Comprehensive Search Result: {'Keyword Search Result': ObjectApiResponse({'took': 202, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0}, 'hits': {'total': {'value': 1, 'relation': 'eq'}, 'max_score': 0.7361701, 'hits': [{'_index': '20251206-233858_test_es_search', '_id': '2', '_score': 0.7361701, '_source': {'title': 'Python a programming', 'content': 'Python is a versatile programming language.', 'vector': [0.4, 0.5, 0.6]}}]}}), 'Structured Search Result': [<Hit(20251206-233858_test_es_search/2): {'title': 'Python a programming', 'content': 'Python is a ve...}>], 'Vector Search Result': [{'title': 'Elasticsearch is powerful', 'content': 'Elasticsearch is a distributed search and analytics engine.', 'vector': [0.1, 0.2, 0.3]}, {'title': 'Python a programming', 'content': 'Python is a versatile programming language.', 'vector': [0.4, 0.5, 0.6]}], 'Vector Search Result on Keyword Search': [{'title': 'Python a programming', 'content': 'Python is a versatile programming language.', 'vector': [0.4, 0.5, 0.6]}]}

"""
