from langchain_elasticsearch import ElasticsearchStore
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('moka-ai/m3e-small')

def get_embedding(text):
    vecs = model.encode(text).tolist()
    return vecs

# 1. 连接 ES
es_store = ElasticsearchStore(
    es_url="http://localhost:9200",
    index_name="rag_docs",
    # embedding=OpenAIEmbeddings(),
    embedding=model,
    es_user="elastic",
    es_password="changeme"
)

# 2. 定义双路召回的检索器
# 使用 "hybrid" 策略，这会自动调用 ES 的 query + knn + rrf
retriever = es_store.as_retriever(
    search_type="similarity", # LangChain 接口参数，实际内部逻辑由 strategy 决定
    search_kwargs={
        "k": 5,
        # 开启混合检索模式 (Hybrid Search)
        # 这里的 fetch_k 指的是每一路召回的数量
        "hybrid_search": True, 
        # RRF 参数 (ES 8.8+ 默认开启)
    }
)

# 3. 也可以完全自定义查询 Body (最灵活的工业级做法)
# 很多时候 LangChain 封装的默认逻辑不够用，我们直接传 body
def custom_hybrid_search(query_vector, query_text):
    return {
        "query": {"match": {"content": query_text}},
        "knn": {
            "field": "embedding",
            "query_vector": query_vector,
            "k": 20,
            "num_candidates": 100
        },
        "rank": {"rrf": {}}
    }

# 高级用法：直接调 client
results = es_store.client.search(
    index="rag_docs",
    body=custom_hybrid_search(
        get_embedding("query"), 
        "query"
    )
)
print(results)

