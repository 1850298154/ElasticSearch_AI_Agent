import os  # 用于访问操作系统环境变量
from dotenv import load_dotenv  # 用于加载 .env 文件中的环境变量
from langchain.chat_models import ChatOpenAI  # LangChain 的 ChatOpenAI 模型，用于与 OpenAI 的聊天模型交互
from elasticsearch import Elasticsearch  # Elasticsearch 客户端库，用于与 Elasticsearch 交互

# 加载 .env 文件中的环境变量
load_dotenv()

class Config:
    """
    配置类，用于加载和管理应用程序所需的所有配置。
    """
    # Elasticsearch 服务器地址，从环境变量 ELASTIC_SERVER 中获取
    elastic_server = os.getenv("ELASTIC_SERVER")
    # Elasticsearch 用户名，从环境变量 ELASTIC_USER 中获取
    elastic_user = os.getenv("ELASTIC_USER")
    # Elasticsearch 密码，从环境变量 ELASTIC_PASSWORD 中获取
    elastic_password = os.getenv("ELASTIC_PASSWORD")
    # CA 证书路径，用于验证 Elasticsearch 的 SSL 连接，从环境变量 CA_CERTS 中获取
    ca_certs = os.getenv("CA_CERTS")
    # 证书指纹，用于验证 Elasticsearch 的 SSL 连接，从环境变量 CERT_FINGERPRINT 中获取
    cert_fingerprint = os.getenv("CERT_FINGERPRINT")
    # 是否验证 Elasticsearch 的 SSL 证书，从环境变量 ELASTIC_VERIFY_CERTIFICATES 中获取
    elastic_verify_certificates = os.getenv("ELASTIC_VERIFY_CERTIFICATES") == "true"

    # 初始化 Elasticsearch 客户端
    es = Elasticsearch(
        [elastic_server],  # Elasticsearch 服务器地址
        basic_auth=(elastic_user, elastic_password),  # 基本认证，使用用户名和密码
        ssl_assert_fingerprint=cert_fingerprint,  # 使用证书指纹进行 SSL 验证
        http_compress=True  # 启用 HTTP 压缩
    )

    # Elasticsearch 索引数据的起始位置，从环境变量 ELASTIC_INDEX_DATA_FROM 中获取
    elastic_index_data_from = int(os.getenv("ELASTIC_INDEX_DATA_FROM"))
    # Elasticsearch 索引数据的大小，从环境变量 ELASTIC_INDEX_DATA_SIZE 中获取
    elastic_index_data_size = int(os.getenv("ELASTIC_INDEX_DATA_SIZE"))
    # Elasticsearch 索引数据的最大大小，从环境变量 ELASTIC_INDEX_DATA_MAX_SIZE 中获取
    elastic_index_data_max_size = int(os.getenv("ELASTIC_INDEX_DATA_MAX_SIZE"))

    # OpenAI 模型名称，从环境变量 OPENAI_MODEL 中获取
    model = os.getenv("OPENAI_MODEL")
    # 请求超时时间，从环境变量 REQUEST_TIMEOUT 中获取
    request_timeout = int(os.getenv("REQUEST_TIMEOUT"))
    # 是否启用 LangChain 缓存，从环境变量 LANGCHAIN_CACHE 中获取
    has_langchain_cache = os.getenv("LANGCHAIN_CACHE") == "true"
    # 是否启用 ChatGPT 的流式输出，从环境变量 CHATGPT_STREAMING 中获取
    streaming = os.getenv("CHATGPT_STREAMING") == "true"

    # 初始化 LangChain 的 ChatOpenAI 模型
    llm = ChatOpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),  # OpenAI API 密钥，从环境变量 OPENAI_API_KEY 中获取
        model=model,  # 使用的 OpenAI 模型
        temperature=0,  # 温度参数，控制生成文本的随机性，0 表示完全确定性
        request_timeout=request_timeout,  # 请求超时时间
        cache=has_langchain_cache,  # 是否启用缓存
        streaming=streaming,  # 是否启用流式输出
        verbose=os.getenv("LLM_VERBOSE") == "true"  # 是否启用详细日志，从环境变量 LLM_VERBOSE 中获取
    )

    # 是否启用 LangChain 的详细日志，从环境变量 LANGCHAIN_VERBOSE 中获取
    langchain_verbose = os.getenv("LANGCHAIN_VERBOSE") == "true"
    # Elasticsearch 聚合查询的限制，从环境变量 AGGS_LIMIT 中获取
    aggs_limit = int(os.getenv("AGGS_LIMIT"))
    # 令牌限制，从环境变量 TOKEN_LIMIT 中获取
    token_limit = int(os.getenv("TOKEN_LIMIT"))
    # 最大搜索重试次数，从环境变量 MAX_SEARCH_RETRIES 中获取
    max_search_retries = int(os.getenv("MAX_SEARCH_RETRIES"))

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