# //// filepath: d:\zyt\git_ln\elasticsearch-agent\elasticsearch_agent\tools\bulk_insert_documents_tool.py
import sys
sys.path.append('d:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent')
sys.path.append('d:/zyt/git_ln/elasticsearch-agent/')
print('sys.path')
print(sys.path)

from typing import Type, Optional, List, Dict, Any
from pydantic import BaseModel, Field
from langchain.tools.base import BaseTool
from langchain.callbacks.manager import AsyncCallbackManagerForToolRun
from elasticsearch_agent.config import cfg  # 访问已经初始化好的 Elasticsearch 客户端
from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk
from elasticsearch.exceptions import TransportError
import json
from io import StringIO

from elasticsearch_agent.log_init import logger  # 统一日志

class BulkInsertDocumentsInput(BaseModel):
    """
    定义工具的输入数据模型。
    只有一个字段 bulk_operations，便于像示例 list_indices_tool 一样直接传入一个字符串。
    """
    bulk_operations: str = Field(
        ...,
        description="符合 Elasticsearch _bulk API 的 NDJSON 字符串（动作行与文档行交替，最后需换行）"
    )


class BulkInsertDocumentsTool(BaseTool):
    """
    用于执行 Elasticsearch _bulk 批量写入的工具。
    输入是一段 NDJSON（换行分隔）字符串，内部会直接调用 bulk API。
    """

    name: str = "elastic_bulk_insert_documents"
    description: str = (
        "输入是一个符合 Elasticsearch _bulk API 的 NDJSON 字符串（每个 action 行后跟一行文档），"
        "输出是成功/失败统计。始终用于需要批量写入多个文档（含指定 _id）的场景。"
    )

    args_schema: Optional[Type[BaseModel]] = BulkInsertDocumentsInput

    def _run(
        self,
        bulk_operations: str
    ) -> str:
        """
        同步运行方法：执行批量写入。
        bulk_operations: NDJSON 字符串（注意最后必须以换行结尾）
        """
        es: Elasticsearch = cfg.es

        # 保证最后有换行（_bulk API 要求）
        if not bulk_operations.endswith("\n"):
            bulk_operations += "\n"

        # 统计
        success = 0
        failed = 0
        errors: List[str] = []

        # 将 NDJSON 字符串解析为 action/doc 迭代器以使用 streaming_bulk（更健壮）
        def iter_actions():
            """
            将用户传入的 NDJSON 文本解析成 streaming_bulk 可消费的 action dict。
            支持典型 { "index": { "_index": "...", "_id": "..." } } + 下一行文档。
            """
            buffer = StringIO(bulk_operations)
            while True:
                action_line = buffer.readline()
                if not action_line:
                    break
                action_line = action_line.strip()
                if not action_line:
                    continue
                try:
                    action_meta = json.loads(action_line)
                except json.JSONDecodeError as e:
                    errors.append(f"解析 action 行失败: {action_line} | 错误: {e}")
                    continue

                # 对应的文档行（可能为空，如 delete）
                doc_line = None
                # 仅当动作不是 delete 时，才读取下一行文档
                if "delete" not in action_meta:
                    doc_line = buffer.readline()
                    if not doc_line:
                        errors.append(f"动作后缺少文档行: {action_line}")
                        continue
                    doc_line = doc_line.strip()
                    try:
                        doc_source = json.loads(doc_line)
                    except json.JSONDecodeError as e:
                        errors.append(f"解析文档行失败: {doc_line} | 错误: {e}")
                        continue
                else:
                    doc_source = None

                # 识别动作类型（index / create / update / delete）
                if len(action_meta) != 1:
                    errors.append(f"动作行格式不正确: {action_line}")
                    continue
                action_type, meta = next(iter(action_meta.items()))

                action_dict: Dict[str, Any] = {
                    "_op_type": action_type,
                    "_index": meta.get("_index")
                }
                if "_id" in meta:
                    action_dict["_id"] = meta["_id"]

                if action_type in ("index", "create"):
                    action_dict["_source"] = doc_source
                elif action_type == "update":
                    # update 需要包装在 doc 里
                    action_dict["doc"] = doc_source
                    action_dict["doc_as_upsert"] = True
                elif action_type == "delete":
                    pass
                else:
                    errors.append(f"不支持的操作类型: {action_type}")
                    continue

                yield action_dict

        try:
            for ok, item in streaming_bulk(
                client=es,
                actions=iter_actions(),
                raise_on_error=False,
                raise_on_exception=False,
                chunk_size=500
            ):
                if ok:
                    success += 1
                else:
                    failed += 1
                    # item 结构: {'index': {'_index': 'people', '_id': '1', 'status': 400, 'error': {...}}}
                    op_type, detail = next(iter(item.items()))
                    err_info = detail.get("error")
                    if err_info:
                        errors.append(f"{op_type} {_safe_get(detail,'_index')}/{_safe_get(detail,'_id')} 错误: {err_info}")
        except TransportError as e:
            return f"批量写入请求失败: {e}"

        summary = f"批量写入完成: 成功 {success} 条, 失败 {failed} 条."
        if errors:
            summary += f" 前几条错误: " + " | ".join(errors[:5])
        logger.info(summary)
        return summary

    async def _arun(
        self,
        bulk_operations: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """
        异步运行（当前未实现）。
        """
        raise NotImplementedError("BulkInsertDocumentsTool 不支持异步运行")


def _safe_get(d: Dict[str, Any], key: str) -> Any:
    return d.get(key, "?")


if __name__ == "__main__":
#     """
#     直接运行本文件时，使用题目给出的示例数据进行测试。
#     """
#     # 构造与题目一致的 _bulk NDJSON 字符串
#     bulk_ndjson = """{ "index" : { "_index" : "people", "_id" : "1" } }
# { "name" : "John Doe", "description" : "A software developer", "sex" : "Male", "age" : 30, "address" : "123 Elm Street, Springfield" }
# { "index" : { "_index" : "people", "_id" : "2" } }
# { "name" : "Jane Smith", "description" : "A project manager", "sex" : "Female", "age" : 28, "address" : "456 Maple Avenue, Anytown" }
# { "index" : { "_index" : "people", "_id" : "3" } }
# { "name" : "Alice Johnson", "description" : "A graphic designer", "sex" : "Female", "age" : 26, "address" : "789 Oak Lane, Metropolis" }
# { "index" : { "_index" : "people", "_id" : "4" } }
# { "name" : "Bob Brown", "description" : "A marketing specialist", "sex" : "Male", "age" : 32, "address" : "321 Pine Street, Gotham" }
# { "index" : { "_index" : "people", "_id" : "5" } }
# { "name" : "Charlie Davis", "description" : "An IT analyst", "sex" : "Male", "age" : 29, "address" : "654 Cedar Blvd, Star City" }
# { "index" : { "_index" : "people", "_id" : "6" } }
# { "name" : "Diana Prince", "description" : "A diplomat", "sex" : "Female", "age" : 35, "address" : "987 Birch Road, Themyscira" }
# { "index" : { "_index" : "people", "_id" : "7" } }
# { "name" : "Evan Wright", "description" : "A journalist", "sex" : "Male", "age" : 27, "address" : "213 Willow Lane, Central City" }
# { "index" : { "_index" : "people", "_id" : "8" } }
# { "name" : "Fiona Gallagher", "description" : "A nurse", "sex" : "Female", "age" : 31, "address" : "546 Spruce Street, South Side" }
# { "index" : { "_index" : "people", "_id" : "9" } }
# { "name" : "George King", "description" : "A teacher", "sex" : "Male", "age" : 34, "address" : "879 Elm St, Smallville" }
# { "index" : { "_index" : "people", "_id" : "10" } }
# { "name" : "Helen Parr", "description" : "A full-time superhero", "sex" : "Female", "age" : 37, "address" : "123 Metro Avenue, Metroville" }
# """

#     tool = BulkInsertDocumentsTool()
#     result = tool(bulk_ndjson)  # 只有一个字段，直接传字符串（与 list_indices_tool 风格一致）
#     logger.info(result)
    

    # 新增：向 example_vector_index 插入向量示例文档

    vector_bulk_ndjson = """{ "index": { "_index": "example_vector_index" } }
{ "name": "苹果", "embedding": [0.2, 0.1, 0.4] }
{ "index": { "_index": "example_vector_index" } }
{ "name": "小船", "embedding": [0.7, 0.2, 0.6] }
{ "index": { "_index": "example_vector_index" } }
{ "name": "香蕉", "embedding": [0.3, 0.1, 0.3] }
"""
    tool = BulkInsertDocumentsTool()
    result_vector = tool(vector_bulk_ndjson)
    logger.info(result_vector)

