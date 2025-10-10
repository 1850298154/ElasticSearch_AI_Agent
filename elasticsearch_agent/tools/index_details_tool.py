import sys
sys.path.append('d:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent')
sys.path.append('d:/zyt/git_ln/elasticsearch-agent/')
print('sys.path')
print(sys.path)


from typing import Type, Optional  # 用于类型注解，Type 表示类型，Optional 表示可选值

from pydantic import BaseModel, Field  # Pydantic 是一个数据验证和设置管理库，BaseModel 是其基础类，Field 用于字段定义

from langchain.callbacks.manager import (  # LangChain 的回调管理器，用于工具运行时的回调管理
    AsyncCallbackManagerForToolRun,  # 异步回调管理器
    CallbackManagerForToolRun,  # 同步回调管理器
)

from elasticsearch_agent.config import cfg  # 导入配置类实例 cfg，用于访问 Elasticsearch 配置
from langchain.tools.base import BaseTool  # LangChain 的工具基类，所有工具都需要继承此类
from elasticsearch_agent.log_init import logger  # 导入日志记录器，用于记录日志信息


class IndexDetailsInput(BaseModel):
    """
    定义工具的输入数据模型。
    继承自 Pydantic 的 BaseModel，用于验证输入数据的结构和类型。
    """

    index_name: str = Field(
        ...,  # 表示该字段为必填项
        description="要检索详细信息的索引名称"  # 字段的描述信息，用于说明字段的用途
    )


class IndexDetailsTool(BaseTool):
    """
    用于获取单个 Elasticsearch 索引详细信息的工具。
    该工具可以返回索引的别名、字段映射和设置等信息。
    """

    # 工具的名称，用于标识该工具
    name: str = "elastic_index_show_details"
    # 工具的描述信息，说明工具的输入和输出
    description: str = "输入是索引名称，输出是一个基于 JSON 的字符串，包含索引的别名、字段映射和设置等详细信息"

    def _run(
        self,
        index_name: str,  # 索引名称，指定要检索详细信息的 Elasticsearch 索引
        run_manager: Optional[CallbackManagerForToolRun] = None,  # 可选的回调管理器，用于工具运行时的回调管理
    ) -> str:
        """
        工具的运行方法，用于从 Elasticsearch 中检索索引的详细信息。
        """
        try:
            # 获取索引的别名信息
            alias = cfg.es.indices.get_alias(index=index_name)
            # 获取索引的字段映射信息
            field_mappings = cfg.es.indices.get_field_mapping(
                index=index_name, fields="*"  # 查询所有字段的映射
            )
            # 获取索引的设置信息
            field_settings = cfg.es.indices.get_settings(index=index_name)
            # 返回包含别名、字段映射和设置的 JSON 字符串
            return str(
                {
                    "alias": alias[index_name],  # 索引的别名信息
                    "field_mappings": field_mappings[index_name],  # 索引的字段映射信息
                    "settings": field_settings[index_name],  # 索引的设置信息
                }
            )
        except:
            # 如果查询失败，记录异常日志
            logger.exception(f"无法获取索引 {index_name} 的详细信息")
            return ""  # 返回空字符串表示失败

    async def _arun(
        self,
        index_name: str = "",  # 异步方法的索引名称参数
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,  # 异步回调管理器
    ) -> str:
        """
        异步运行方法。
        当前工具不支持异步运行，因此抛出 NotImplementedError。
        """
        raise NotImplementedError("IndexDetailsTool 不支持异步运行")

    # 定义工具的输入数据模型，用于验证输入数据的结构
    args_schema: Optional[Type[BaseModel]] = IndexDetailsInput


if __name__ == "__main__":
    """
    如果直接运行此文件，执行以下代码。
    """
    # 定义要查询的索引名称
    index_name = "socio_economic_indicators"
    index_name = "example_vector_index"
    # 创建工具实例
    tool = IndexDetailsTool()
    # 运行工具并获取结果
    result = tool(index_name)
    # 记录查询结果
    logger.info("result: %s", result)
    
"""
{
    "example_vector_index":{
        "mappings":{
            "properties":{
                "embedding":{
                    "type":"float"
                },
                "embeding":{
                    "type":"dense_vector",
                    "dims":3,
                    "index":true,
                    "similarity":"cosine",
                    "index_options":{
                        "type":"int8_hnsw",
                        "m":16,
                        "ef_construction":100
                    }
                },
                "name":{
                    "type":"text"
                }
            }
        }
    }
}
"""