import sys
sys.path.append('d:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent')
sys.path.append('d:/zyt/git_ln/elasticsearch-agent/')
print('sys.path')
print(sys.path)

from typing import Optional, Type, Dict, Any
from pydantic import BaseModel, Field
from langchain.tools import BaseTool
from langchain_core.callbacks import AsyncCallbackManagerForToolRun
from elasticsearch_agent.config import cfg
from elasticsearch_agent.log_init import logger


class CreateIndexInput(BaseModel):
    """
    创建索引工具的输入数据模型。
    """
    index_name: str = Field(..., description="要创建的索引名称")
    body: Optional[Dict[str, Any]] = Field(
        default=None,
        description="可选的索引定义（包含 settings, mappings 等）"
    )


class CreateIndexTool(BaseTool):
    """
    用于创建 Elasticsearch 索引的工具。
    如果索引已存在，则返回提示信息。
    """
    name: str = "elastic_create_index"
    description: str = (
        "输入是索引名称和可选的索引结构 body（包含 settings 和 mappings）。"
        "使用此工具在 Elasticsearch 中创建一个索引；如果索引已存在，会返回已存在信息。"
    )

    args_schema: Optional[Type[BaseModel]] = CreateIndexInput

    def _run(
        self,
        index_name: str,
        body: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        创建索引的同步方法。
        """
        try:
            if cfg.es.indices.exists(index=index_name):
                return f"Index '{index_name}' already exists."

            if body:
                cfg.es.indices.create(index=index_name, body=body)
            else:
                cfg.es.indices.create(index=index_name)

            return f"Index '{index_name}' created successfully."
        except Exception as e:
            logger.exception("Failed to create index '%s': %s", index_name, e)
            return f"Failed to create index '{index_name}': {e}"

    async def _arun(
        self,
        index_name: str,
        body: Optional[Dict[str, Any]] = None,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """
        异步运行方法（当前未实现）。
        """
        raise NotImplementedError("CreateIndexTool 不支持异步运行")

from elasticsearch_agent.tools.create_index_tool import CreateIndexTool

def test_vector_index_creation():
    tool = CreateIndexTool()
    
    vector_index_name = "example_vector_index"
    vector_body = {
        "mappings": {
            "properties": {
                "name": {
                    "type": "text"
                },
                "embedding": {
                    "type": "dense_vector",
                    "dims": 3
                }
            }
        }
    }

    result = tool._run(index_name=vector_index_name, body=vector_body)
    print('result of test_vector_index_creation:')
    print(result)
    # assert "created successfully" in result

# def test_hybrid_index_creation():
#     tool = CreateIndexTool()
    
#     hybrid_index_name = "example_hybrid_index"
#     hybrid_body = {
#         "mappings": {
#             "properties": {
#                 "vector_field": {
#                     "type": "knn_vector",
#                     "dimension": 3
#                 },
#                 "text_field": {
#                     "type": "text"
#                 },
#                 "metadata": {
#                     "type": "text"
#                 }
#             }
#         }
#     }

#     result = tool._run(index_name=hybrid_index_name, body=hybrid_body)
#     print('result of test_hybrid_index_creation:')
#     print(result)

if __name__ == "__main__":
    # """
    # 测试示例：定义索引结构并创建索引。
    # """
    # tool = CreateIndexTool()

    # example_index = "example_create_index"

    # example_body = {
    #     "settings": {
    #         "number_of_shards": 1,
    #         "number_of_replicas": 0,
    #         "analysis": {
    #             "analyzer": {
    #                 "default": {
    #                     "type": "standard"
    #                 }
    #             }
    #         }
    #     },
    #     "mappings": {
    #         "properties": {
    #             "title": {"type": "text"},
    #             "content": {"type": "text"},
    #             "published_at": {"type": "date"},
    #             "tags": {"type": "keyword"},
    #             "views": {"type": "integer"}
    #         }
    #     }
    # }

    # result = tool._run(index_name=example_index, body=example_body)
    # logger.info(result)
    test_vector_index_creation()
    # test_hybrid_index_creation()