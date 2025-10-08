import sys
sys.path.append('d:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent')
sys.path.append('d:/zyt/git_ln/elasticsearch-agent/')
print('sys.path')
print(sys.path)

from typing import Type, Optional, List  # 用于类型注解，Type 表示类型，Optional 表示可选值，List 表示列表类型

from pydantic import BaseModel, Field  # Pydantic 是一个数据验证和设置管理库，BaseModel 是其基础类，Field 用于字段定义
from langchain.tools.base import BaseTool  # LangChain 的工具基类，所有工具都需要继承此类
from langchain.callbacks.manager import (  # LangChain 的回调管理器，用于工具运行时的回调管理
    AsyncCallbackManagerForToolRun  # 异步回调管理器
)

from elasticsearch_agent.config import cfg  # 导入配置类实例 cfg，用于访问 Elasticsearch 配置


class ListIndicesInput(BaseModel):
    """
    定义工具的输入数据模型。
    继承自 Pydantic 的 BaseModel，用于验证输入数据的结构和类型。
    """

    separator: str = Field(
        ...,  # 表示该字段为必填项
        description="用于分隔索引列表的分隔符"  # 字段的描述信息，用于说明字段的用途
    )


class ListIndicesTool(BaseTool):
    """
    用于获取 Elasticsearch 集群中所有索引的工具。
    """

    # 工具的名称，用于标识该工具
    name: str = "elastic_list_indices"
    # 工具的描述信息，说明工具的输入和输出
    description: str = (
        "输入是一个分隔符（例如逗号或换行符），输出是一个以分隔符分隔的索引列表。"
        "始终使用此工具来了解 Elasticsearch 集群中的索引。"
    )

    def _run(
        self,
        separator: str  # 分隔符，用于分隔返回的索引列表
    ) -> str:
        """
        工具的运行方法，用于从 Elasticsearch 中获取所有索引。
        """
        # 使用 Elasticsearch 客户端获取所有索引的名称
        indices: List[str] = cfg.es.cat.indices(h="index", s="index").split()
        # 过滤掉以 "." 开头的系统索引，并使用指定的分隔符连接索引名称
        return separator.join(
            [index for index in indices if not index.startswith(".")]
        )

    async def _arun(
        self,
        separator: str = "",  # 异步方法的分隔符参数
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,  # 异步回调管理器
    ) -> str:
        """
        异步运行方法。
        当前工具不支持异步运行，因此抛出 NotImplementedError。
        """
        raise NotImplementedError("ListIndicesTool 不支持异步运行")

    # 定义工具的输入数据模型，用于验证输入数据的结构
    args_schema: Optional[Type[BaseModel]] = ListIndicesInput


if __name__ == "__main__":
    """
    如果直接运行此文件，执行以下代码。
    """
    from elasticsearch_agent.log_init import logger  # 导入日志记录器，用于记录日志信息

    # 创建工具实例
    indices_tool = ListIndicesTool()
    # 使用工具获取索引列表，并记录结果
    logger.info(indices_tool(","))