# Elasticsearch Langchain Agent (Enhanced version by Yuteng Zhao)
 
## third development with more tools (insert tool etc.)

This project uses ElasticSearch together with LangChain and ChatGPT 4 to build an agent with which you can ask intelligent questions on
top of an ElasticSearch cluster.

## output
The server output will be like ref: [output2.md](output2.md)

front end output will be like:
![alt text](zfig/README/image.png)



## Setup

start with command:

```
python  elasticsearch_agent/agent/test/agent_factory_test.py
```

## env

The configuration should be saved in a `kv.py` file.

kv = {
    "ELASTIC_SERVER": "https://localhost:9200",
    "ELASTIC_USER": "elastic",
    "ELASTIC_PASSWORD": "",
    "CERT_FINGERPRINT": "",
    "ELASTIC_VERIFY_CERTIFICATES": "true",
    "ELASTIC_INDEX_DATA_FROM": "0",
    "ELASTIC_INDEX_DATA_SIZE": "100",
    "ELASTIC_INDEX_DATA_MAX_SIZE": "1000",
    "OPENAI_MODEL": "qwen-plus",
    "REQUEST_TIMEOUT": "30",
    "LANGCHAIN_CACHE": "true",
    "CHATGPT_STREAMING": "false",
    "OPENAI_API_KEY": "",
    "LLM_VERBOSE": "false",
    "LANGCHAIN_VERBOSE": "true",
    "AGGS_LIMIT": "10",
    "TOKEN_LIMIT": "2048",
    "MAX_SEARCH_RETRIES": "3"
}