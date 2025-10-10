import sys
sys.path.append('d:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent')
sys.path.append('d:/zyt/git_ln/elasticsearch-agent/')
print('sys.path')
print(sys.path)


from typing import Type, Optional  # 用于类型注解，Type 表示类型，Optional 表示可选值

from langchain.callbacks.manager import CallbackManagerForToolRun  # LangChain 的回调管理器，用于工具运行时的回调管理

from pydantic import BaseModel, Field  # Pydantic 是一个数据验证和设置管理库，BaseModel 是其基础类，Field 用于字段定义

from langchain.tools.base import BaseTool  # LangChain 的工具基类，所有工具都需要继承此类

from elasticsearch_agent.log_init import logger  # 导入日志记录器，用于记录日志信息
from elasticsearch_agent.config import cfg  # 导入配置类实例 cfg，用于访问配置参数


class IndexShowDataInput(BaseModel):
    """
    定义工具的输入数据模型。
    继承自 Pydantic 的 BaseModel，用于验证输入数据的结构和类型。
    """

    index_name: str = Field(
        ...,  # 表示该字段为必填项
        description="要检索数据的索引名称"  # 字段的描述信息，用于说明字段的用途
    )


class IndexShowDataTool(BaseTool):
    """
    用于从 Elasticsearch 索引中获取数据的工具。
    该工具可以帮助用户了解索引中可用的数据。
    """

    # 工具的名称，用于标识该工具
    name: str = "elastic_index_show_data"
    # 工具的描述信息，说明工具的输入和输出
    description: str = "输入是索引名称，输出是一个基于 JSON 的字符串，包含索引数据的提取内容"

    def _run(
        self,
        index_name: str,  # 索引名称，指定要检索数据的 Elasticsearch 索引
        run_manager: Optional[CallbackManagerForToolRun] = None,  # 可选的回调管理器，用于工具运行时的回调管理
    ) -> str:
        """
        工具的运行方法，用于从 Elasticsearch 中检索数据。
        """
        try:
            # 使用配置中的 Elasticsearch 客户端执行搜索查询
            res = cfg.es.search(
                index=index_name,  # 指定要查询的索引名称
                from_=cfg.elastic_index_data_from,  # 查询结果的起始位置，从配置中获取
                size=cfg.elastic_index_data_size,  # 查询结果的大小，从配置中获取
                query={"match_all": {}},  # 查询条件，这里是匹配所有文档
            )
            # 返回查询结果中的 hits 部分，转换为字符串格式
            return str(res["hits"])
        except:
            # 如果查询失败，记录异常日志
            logger.exception(f"无法获取索引 {index_name} 的数据")
            return ""  # 返回空字符串表示失败

    # 定义工具的输入数据模型，用于验证输入数据的结构
    args_schema: Optional[Type[BaseModel]] = IndexShowDataInput


if __name__ == "__main__":
    """
    如果直接运行此文件，执行以下代码。
    """
    # 定义要查询的索引名称
    index_name = "socio_economic_indicators"
    index_name = "example_vector_index"
    # 创建工具实例并运行查询
    res = IndexShowDataTool().run(index_name)
    # 记录查询结果
    logger.info(res)