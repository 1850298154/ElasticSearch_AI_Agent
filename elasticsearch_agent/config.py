import os  # 用于访问操作系统环境变量
from dotenv import load_dotenv  # 用于加载 .env 文件中的环境变量
from langchain.chat_models import ChatOpenAI  # LangChain 的 ChatOpenAI 模型，用于与 OpenAI 的聊天模型交互
# from graphrag.query.llm.oai.chat_openai import ChatOpenAI

from elasticsearch import Elasticsearch  # Elasticsearch 客户端库，用于与 Elasticsearch 交互
from kv import kv  # 导入 kv 模块

# 加载 .env 文件中的环境变量
load_dotenv()

class Config:
    """
    配置类，用于加载和管理应用程序所需的所有配置。
    """
    # Elasticsearch 服务器地址，从环境变量 ELASTIC_SERVER 中获取
    elastic_server = kv.get("ELASTIC_SERVER")
    # Elasticsearch 用户名，从环境变量 ELASTIC_USER 中获取
    elastic_user = kv.get("ELASTIC_USER")
    # Elasticsearch 密码，从环境变量 ELASTIC_PASSWORD 中获取
    elastic_password = kv.get("ELASTIC_PASSWORD")
    # CA 证书路径，用于验证 Elasticsearch 的 SSL 连接，从环境变量 CA_CERTS 中获取
    ca_certs = kv.get("CA_CERTS")
    # 证书指纹，用于验证 Elasticsearch 的 SSL 连接，从环境变量 CERT_FINGERPRINT 中获取
    cert_fingerprint = kv.get("CERT_FINGERPRINT")
    # 是否验证 Elasticsearch 的 SSL 证书，从环境变量 ELASTIC_VERIFY_CERTIFICATES 中获取
    elastic_verify_certificates = kv.get("ELASTIC_VERIFY_CERTIFICATES") == "true"

    # 初始化 Elasticsearch 客户端
    es = Elasticsearch(
        [elastic_server],  # Elasticsearch 服务器地址
        basic_auth=(elastic_user, elastic_password),  # 基本认证，使用用户名和密码
        ssl_assert_fingerprint=cert_fingerprint,  # 使用证书指纹进行 SSL 验证
        http_compress=True  # 启用 HTTP 压缩
    )

    # Elasticsearch 索引数据的起始位置，从环境变量 ELASTIC_INDEX_DATA_FROM 中获取
    elastic_index_data_from = int(kv.get("ELASTIC_INDEX_DATA_FROM"))
    # Elasticsearch 索引数据的大小，从环境变量 ELASTIC_INDEX_DATA_SIZE 中获取
    elastic_index_data_size = int(kv.get("ELASTIC_INDEX_DATA_SIZE"))
    # Elasticsearch 索引数据的最大大小，从环境变量 ELASTIC_INDEX_DATA_MAX_SIZE 中获取
    elastic_index_data_max_size = int(kv.get("ELASTIC_INDEX_DATA_MAX_SIZE"))

    # OpenAI 模型名称，从环境变量 OPENAI_MODEL 中获取
    model = kv.get("OPENAI_MODEL")
    # 请求超时时间，从环境变量 REQUEST_TIMEOUT 中获取
    request_timeout = int(kv.get("REQUEST_TIMEOUT"))
    # 是否启用 LangChain 缓存，从环境变量 LANGCHAIN_CACHE 中获取
    has_langchain_cache = kv.get("LANGCHAIN_CACHE") == "true"
    # 是否启用 ChatGPT 的流式输出，从环境变量 CHATGPT_STREAMING 中获取
    streaming = kv.get("CHATGPT_STREAMING") == "true"

    # # 初始化 LangChain 的 ChatOpenAI 模型
    llm = ChatOpenAI(
        openai_api_base="http://localhost:3000/v1",  # 自定义 URL（需包含 API 版本路径，如 /v1）
        # openai_api_key=kv.get("OPENAI_API_KEY"),  # OpenAI API 密钥，从环境变量 OPENAI_API_KEY 中获取
        openai_api_key="sk-n6prRwyWRItnjkWT2e9d295a40C14752A48367D0718a6bC9",  # OpenAI API 密钥，从环境变量 OPENAI_API_KEY 中获取
        model="qwen-plus",  # 使用的 OpenAI 模型
        # temperature=0,  # 温度参数，控制生成文本的随机性，0 表示完全确定性
        request_timeout=request_timeout,  # 请求超时时间
        # cache=has_langchain_cache,  # 是否启用缓存
        cache=False,  # 禁用缓存
        # streaming=streaming,  # 是否启用流式输出
        # verbase=True,  # 启用详细日志
        # verbose=kv.get("LLM_VERBOSE") == "true"  # 是否启用详细日志，从环境变量 LLM_VERBOSE 中获取
    )
    # from enum import Enum
    # from typing import Any, cast
    # import openai
    # class OpenaiApiType(str, Enum):
    #     """The OpenAI Flavor."""

    #     OpenAI = "openai"
    #     AzureOpenAI = "azure"
    # llm = ChatOpenAI(
    #     # # 调用gpt
    #     # api_base="https://api.wlai.vip/v1",  # 请求的API服务地址
    #     # api_key="sk-4P8HC2GD6heTwx0l8dD83f13F1014e039eC4Ac6d47877dCb",  # API Key
    #     # model="gpt-4o-mini",  # 本次使用的模型
    #     # api_type=OpenaiApiType.OpenAI,

    #     # # 调用其他模型  通过oneAPI
    #     # api_base="http://139.224.72.218:3000/v1",  # 请求的API服务地址
    #     # api_key="sk-KtEtYw4jOGtSpr4n2e06Ee978690452183Be8a1fF75cA8C5",  # API Key
    #     # model="qwen-plus",  # 本次使用的模型
    #     # api_type=OpenaiApiType.OpenAI,

    #     # 调用本地大模型  通过Ollama
    #     api_base="http://localhost:3000/v1",  # 请求的API服务地址
    #     api_key="sk-n6prRwyWRItnjkWT2e9d295a40C14752A48367D0718a6bC9",  # API Key
    #     model="qwen-plus",  # 本次使用的模型
    #     api_type=OpenaiApiType.OpenAI,
    # )
    # 是否启用 LangChain 的详细日志，从环境变量 LANGCHAIN_VERBOSE 中获取
    langchain_verbose = kv.get("LANGCHAIN_VERBOSE") == "true"
    # Elasticsearch 聚合查询的限制，从环境变量 AGGS_LIMIT 中获取
    aggs_limit = int(kv.get("AGGS_LIMIT"))
    # 令牌限制，从环境变量 TOKEN_LIMIT 中获取
    token_limit = int(kv.get("TOKEN_LIMIT"))
    # 最大搜索重试次数，从环境变量 MAX_SEARCH_RETRIES 中获取
    max_search_retries = int(kv.get("MAX_SEARCH_RETRIES"))

# 创建 Config 类的实例
cfg = Config()

if __name__ == "__main__":
    # 如果直接运行此文件，执行以下代码
    from elasticsearch_agent.log_init import logger  # 导入日志记录器

    # 定义需要检查的字段
    check_fields = [
        cfg.elastic_server,  # 检查 Elasticsearch 服务器地址
        cfg.elastic_user,  # 检查 Elasticsearch 用户名
        cfg.elastic_password,  # 检查 Elasticsearch 密码
        cfg.elastic_verify_certificates,  # 检查是否验证 SSL 证书
        cfg.elastic_index_data_from,  # 检查索引数据的起始位置
        cfg.elastic_index_data_size  # 检查索引数据的大小
    ]
    # 遍历检查字段，确保它们不为空
    for field in check_fields:
        assert field is not None  # 如果字段为空，抛出 AssertionError
        logger.info(field)  # 记录字段的值