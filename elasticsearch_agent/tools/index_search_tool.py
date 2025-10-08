import sys
sys.path.append('d:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent')
sys.path.append('d:/zyt/git_ln/elasticsearch-agent/')
print('sys.path')
print(sys.path)


import json  # 用于处理 JSON 数据

from pydantic.v1 import BaseModel, Field  # Pydantic v1，用于数据验证和字段定义

import tiktoken  # 用于对文本进行编码，计算令牌数量

from elasticsearch_agent.log_init import logger  # 导入日志记录器，用于记录日志信息
from elasticsearch_agent.config import cfg  # 导入配置类实例 cfg，用于访问配置参数

from langchain.tools import StructuredTool  # LangChain 的工具类，用于创建结构化工具


class SearchToolInput(BaseModel):
    """
    定义工具的输入数据模型。
    继承自 Pydantic 的 BaseModel，用于验证输入数据的结构和类型。
    一个完整的举例：
     '{"index_name": "index_name", "query": "{\\"size\\": 0, \\"aggs\\" : { \\"regions\\" : { \\"terms\\" : { \\"field\\" : \\"region\\", \\"size\\": 100 } } } }", "from_": 0, "size": 10}'
    """

    index_name: str = Field(
        ...,  # 表示该字段为必填项
        description="要检索数据的索引名称"  # 字段的描述信息，用于说明字段的用途
    )
    query: str = Field(
        ...,  # 表示该字段为必填项
        description="用于过滤所有命中的 Elasticsearch JSON 查询。尽可能使用 _source 字段指定所需字段"  # 字段的描述信息
    )
    from_: int = Field(
        ...,  # 表示该字段为必填项
        description="查询将从哪个记录索引开始"  # 字段的描述信息
    )
    size: int = Field(
        ...,  # 表示该字段为必填项
        description="从 Elasticsearch 查询中检索的记录数量"  # 字段的描述信息
    )


def elastic_search(
    index_name: str,  # 索引名称，指定要查询的 Elasticsearch 索引
    query: str,  # 查询字符串，包含 JSON 格式的查询条件
    from_: int = cfg.elastic_index_data_from,  # 查询结果的起始位置，默认为配置中的值
    size: int = cfg.elastic_index_data_size,  # 查询结果的大小，默认为配置中的值
):
    """
    在 Elasticsearch 索引上执行特定查询，并返回所有命中或聚合结果。
    """
    # 确保查询的大小不超过配置中允许的最大值
    size = min(cfg.elastic_index_data_max_size, size)
    # 获取模型的编码器，用于计算令牌数量
    # encoding = tiktoken.encoding_for_model(cfg.model)
    encoding = tiktoken.get_encoding("cl100k_base")
    try:
        # 将查询字符串解析为字典
        full_dict: dict = json.loads(query)
        query_dict = None  # 查询部分
        aggs_dict = None  # 聚合部分
        sort_dict = None  # 排序部分

        # 检查查询中是否包含 "query"、"aggs" 和 "sort" 部分
        if "query" in full_dict:
            query_dict = full_dict["query"]
        if "aggs" in full_dict:
            aggs_dict = full_dict["aggs"]
        if "sort" in full_dict:
            sort_dict = full_dict["sort"]

        # 如果没有明确的查询部分，但有聚合部分，则假定为聚合查询
        if query_dict is None and aggs_dict is None and sort_dict is None:
            query_dict = full_dict
        if query_dict is None and aggs_dict is not None:
            size = cfg.aggs_limit  # 如果是聚合查询，限制结果大小为配置中的聚合限制

        # 记录查询日志
        logger.info(query)

        final_res = ""  # 最终结果
        retries = 0  # 重试次数

        # 在配置的最大重试次数内尝试执行查询
        while retries < cfg.max_search_retries:
            # 执行 Elasticsearch 查询
            res = cfg.es.search(
                index=index_name,  # 指定索引名称
                from_=from_,  # 查询起始位置
                size=size,  # 查询结果大小
                query=query_dict,  # 查询条件
                aggs=aggs_dict,  # 聚合条件
                sort=sort_dict,  # 排序条件
            )
            # 如果是聚合查询，返回聚合结果
            if query_dict is None and aggs_dict is not None:
                final_res = str(res["aggregations"])
            else:
                # 否则返回命中结果
                final_res = str(res["hits"])

            # 对结果进行编码，计算令牌数量
            tokens = encoding.encode(final_res)
            retries += 1  # 增加重试次数

            # 如果令牌数量超过限制，减少查询大小并重试
            if len(tokens) > cfg.token_limit:
                size -= 1
            else:
                # 如果令牌数量在限制范围内，返回结果
                return final_res

    except Exception as e:
        # 如果查询失败，记录异常日志
        logger.exception(f"无法执行查询 {query}")
        msg = str(e)  # 获取异常信息
        return msg  # 返回异常信息


def create_search_tool():
    """
    创建搜索工具实例。
    """
    return StructuredTool.from_function(
        elastic_search,  # 工具的功能函数
        name="elastic_index_search_tool",  # 工具的名称
        args_schema=SearchToolInput,  # 工具的输入数据模型
    )


if __name__ == "__main__":
    """
    如果直接运行此文件，执行以下代码。
    """
    # 定义要查询的索引名称
    index_name = "co2_production"
    # 创建搜索工具实例
    tool = create_search_tool()
    # 运行工具并执行查询
    param = {
            "index_name": index_name,  # 索引名称
            "query": """{"size": 0, "aggs" : { "regions" : { "terms" : { "field" : "region", "size": 100 } } } }""",  # 查询条件
            "from_": 0,  # 查询起始位置
            "size": 10,  # 查询结果大小
        }
    print('param', param)
    # res = tool.run(param)    
    # res = elastic_search(**param)       
    # 记录查询结果
    # logger.info(res)
    
    arguments = json.loads('{"index_name": "people", "query": "{\\"size\\": 1, \\"sort\\": [{\\"age\\": {\\"order\\": \\"desc\\"}}], \\"_source\\": [\\"name\\", \\"age\\"]}", "from_": 0, "size": 1}')
    print('arguments', arguments)
    res = tool.run(arguments)
    # res = elastic_search(**arguments)
    # 记录查询结果
    logger.info(res)