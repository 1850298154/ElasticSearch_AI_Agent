import sys
sys.path.append('d:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent')
sys.path.append('d:/zyt/git_ln/elasticsearch-agent/')
print('sys.path')
print(sys.path)

from typing import Optional, Type
from pydantic import BaseModel, Field
from langchain.tools import BaseTool
from langchain_core.callbacks import AsyncCallbackManagerForToolRun
from elasticsearch_agent.config import cfg
from elasticsearch_agent.log_init import logger


class DeleteIndexInput(BaseModel):
    """
    删除索引工具的输入数据模型。
    """
    index_name: str = Field(..., description="要删除的索引名称")


class DeleteIndexTool(BaseTool):
    """
    用于删除 Elasticsearch 索引的工具。
    如果索引不存在，则返回提示信息。
    """
    name: str = "elastic_delete_index"
    description: str = (
        "输入是索引名称。"
        "使用此工具在 Elasticsearch 中删除一个索引；如果索引不存在，会返回不存在信息。"
    )

    args_schema: Optional[Type[BaseModel]] = DeleteIndexInput

    def _run(self, index_name: str) -> str:
        """
        删除索引的同步方法。
        """
        try:
            if not cfg.es.indices.exists(index=index_name):
                return f"Index '{index_name}' does not exist."

            cfg.es.indices.delete(index=index_name)
            return f"Index '{index_name}' deleted successfully."
        except Exception as e:
            logger.exception("Failed to delete index '%s': %s", index_name, e)
            return f"Failed to delete index '{index_name}': {e}"

    async def _arun(self, index_name: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None) -> str:
        """
        异步运行方法（当前未实现）。
        """
        raise NotImplementedError("DeleteIndexTool 不支持异步运行")


def test_delete_index():
    tool = DeleteIndexTool()
    
    index_name_to_delete = "example_vector_index"
    result = tool._run(index_name=index_name_to_delete)
    print('result of test_delete_index:')
    print(result)

if __name__ == "__main__":
    test_delete_index()