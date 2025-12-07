
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from annoy import AnnoyIndex
from sentence_transformers import SentenceTransformer


class ElasticsearchSearch:
    def __init__(self, url):
        self.es = Elasticsearch([url], max_retries=10)
        self.index_name = datetime.now().strftime('%Y%m%d-%H%M%S') + "_test_es_search"

    def create_index(self, mapping):
        self.es.indices.create(index=self.index_name, body=mapping)

    def create_index_zh_en_mixed(self):
        mapping = {
            "settings": {
                "number_of_shards": 1,  # 单节点建议1分片
                "number_of_replicas": 0, # 单节点建议0副本
                "analysis": {
                    # 自定义混合分析器
                    "analyzer": {
                        "zh_en_mixed_analyzer": {
                            "type": "custom",
                            "tokenizer": "ik_smart",  # 核心：IK智能分词（处理中文）
                            "filter": [
                                "lowercase",  # 英文转小写
                                "stop",        # 可选：过滤英文停用词（如 a/an/the）
                                "stemmer",  # 可选：英文词干提取（如 running -> run）
                            ]
                        },
                        # 可选：IK最大词长分词（更细粒度，适合精准检索）
                        "zh_en_max_word_analyzer": {
                            "type": "custom",
                            "tokenizer": "ik_max_word",
                            "filter": ["lowercase"]
                        }
                    }
                }
            },
            "mappings": {
                "properties": {
                    "content": {  # 中英文混合文本字段
                        "type": "text",
                        "analyzer": "zh_en_mixed_analyzer",  # 索引时用智能分词
                        "search_analyzer": "zh_en_mixed_analyzer"  # 搜索时用相同分析器（保证一致）
                    },
                    # 可选：其他字段示例
                    "title": {
                        "type": "text",
                        "analyzer": "zh_en_max_word_analyzer",  # 更细粒度的分词
                        "fields": {
                            "keyword": {  # 保留关键字类型，用于精确匹配
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    },
                    "title-content-embedding": {
                        "type": "dense_vector",
                        "element_type": "float",
                        "dims": 512,
                        "index": True,
                        "similarity": "cosine"
                    },                    
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


# model = SentenceTransformer('moka-ai/m3e-base')
model = SentenceTransformer('moka-ai/m3e-small')
def get_embedding(text):
    vecs = model.encode(text).tolist()
    return vecs

query = "programming"
query_vector = get_embedding(query)
# es_search = ElasticsearchSearch("http://<your_es_account>:<your_es_password>@<your_es_server_ip>:6030")
es_search = ElasticsearchSearch("http://elastic:xxx@localhost:9200")
es_search.create_index_zh_en_mixed()
es_search.insert_data(doc_id=1, doc_body={
    "title": "Elasticsearch is powerful",
    "content": "Elasticsearch is a distributed search and analytics engine.",
    "vector": get_embedding("Elasticsearch is powerful")
})
es_search.insert_data(doc_id=2, doc_body={
    "title": "Python a programming",
    "content": "Python is a versatile programming language.",
    "vector": get_embedding("Python is a versatile programming language.")
})
es_search.refresh_index()
result = es_search.comprehensive_search(query, query_vector)
print("Comprehensive Search Result:", result)






r"""
docker run -d --name es -e "ES_JAVA_OPTS=-Xms512m -Xmx4024m" -e "discovery.type=single-node" -e "xpack.security.enabled=false" -e "xpack.security.transport.ssl.enabled=false" -e "ELASTIC_PASSWORD=xxx" -v es-data4:/home/xxx/es4/data -v es-plugins4:/home/xxx/es4/plugin --privileged -p 9200:9200 -p 9300:9300  elasticsearch:8.16.1


./elasticsearch-plugin install https://release.infinilabs.com/analysis-ik/stable/elasticsearch-analysis-ik-8.16.1.zip


D:\zyt\git_ln\ElasticSearch_AI_Agent> cmd /C "c:\Python313\python.exe c:\Users\zooos\.vscode\extensions\ms-python.debugpy-2025.16.0-win32-x64\bundled\libs\debugpy\launcher 25623 -- D:\zyt\git_ln\ElasticSearch_AI_Agent\test.py "
Comprehensive Search Result: {'Keyword Search Result': ObjectApiResponse({'took': 202, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0}, 'hits': {'total': {'value': 1, 'relation': 'eq'}, 'max_score': 0.7361701, 'hits': [{'_index': '20251206-233858_test_es_search', '_id': '2', '_score': 0.7361701, '_source': {'title': 'Python a programming', 'content': 'Python is a versatile programming language.', 'vector': [0.4, 0.5, 0.6]}}]}}), 'Structured Search Result': [<Hit(20251206-233858_test_es_search/2): {'title': 'Python a programming', 'content': 'Python is a ve...}>], 'Vector Search Result': [{'title': 'Elasticsearch is powerful', 'content': 'Elasticsearch is a distributed search and analytics engine.', 'vector': [0.1, 0.2, 0.3]}, {'title': 'Python a programming', 'content': 'Python is a versatile programming language.', 'vector': [0.4, 0.5, 0.6]}], 'Vector Search Result on Keyword Search': [{'title': 'Python a programming', 'content': 'Python is a versatile programming language.', 'vector': [0.4, 0.5, 0.6]}]}

"""
