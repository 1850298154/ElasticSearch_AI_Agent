
D:\zyt\git_ln\elasticsearch-agent>C:/Python313/python.exe d:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent/agent/test/agent_factory_test.py
sys.path
['d:\\zyt\\git_ln\\elasticsearch-agent\\elasticsearch_agent\\agent\\test', 'C:\\Python313\\python313.zip', 'C:\\Python313\\DLLs', 'C:\\Python313\\Lib', 'C:\\Python313', 'C:\\Users\\zooos\\AppData\\Roaming\\Python\\Python313\\site-packages', 'C:\\Python313\\Lib\\site-packages', 'd:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent', 'd:/zyt/git_ln/elasticsearch-agent/']
d:\zyt/git_ln/elasticsearch-agent\elasticsearch_agent\config.py:3: LangChainDeprecationWarning: Importing chat models from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.chat_models import ChatOpenAI`.

To install langchain-community run `pip install -U langchain-community`.
  from langchain.chat_models import ChatOpenAI  # LangChain 的 ChatOpenAI 模型，用于与 OpenAI 的聊天模型交互
d:\zyt/git_ln/elasticsearch-agent\elasticsearch_agent\config.py:3: LangChainDeprecationWarning: Importing chat models from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.chat_models import ChatOpenAI`.

To install langchain-community run `pip install -U langchain-community`.
  from langchain.chat_models import ChatOpenAI  # LangChain 的 ChatOpenAI 模型，用于与 OpenAI 的聊天模型交互
d:\zyt/git_ln/elasticsearch-agent\elasticsearch_agent\config.py:54: LangChainDeprecationWarning: The class `ChatOpenAI` was deprecated in LangChain 0.0.10 and will be removed in 1.0. An updated version of the class exists in the :class:`~langchain-openai package and should be used instead. To use it run `pip install -U :class:`~langchain-openai` and import as `from :class:`~langchain_openai import ChatOpenAI``.
  llm = ChatOpenAI(
sys.path
['d:\\zyt\\git_ln\\elasticsearch-agent\\elasticsearch_agent\\agent\\test', 'C:\\Python313\\python313.zip', 'C:\\Python313\\DLLs', 'C:\\Python313\\Lib', 'C:\\Python313', 'C:\\Users\\zooos\\AppData\\Roaming\\Python\\Python313\\site-packages', 'C:\\Python313\\Lib\\site-packages', 'd:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent', 'd:/zyt/git_ln/elasticsearch-agent/', 'd:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent', 'd:/zyt/git_ln/elasticsearch-agent/']
sys.path
['d:\\zyt\\git_ln\\elasticsearch-agent\\elasticsearch_agent\\agent\\test', 'C:\\Python313\\python313.zip', 'C:\\Python313\\DLLs', 'C:\\Python313\\Lib', 'C:\\Python313', 'C:\\Users\\zooos\\AppData\\Roaming\\Python\\Python313\\site-packages', 'C:\\Python313\\Lib\\site-packages', 'd:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent', 'd:/zyt/git_ln/elasticsearch-agent/', 'd:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent', 'd:/zyt/git_ln/elasticsearch-agent/', 'd:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent', 'd:/zyt/git_ln/elasticsearch-agent/']
sys.path
['d:\\zyt\\git_ln\\elasticsearch-agent\\elasticsearch_agent\\agent\\test', 'C:\\Python313\\python313.zip', 'C:\\Python313\\DLLs', 'C:\\Python313\\Lib', 'C:\\Python313', 'C:\\Users\\zooos\\AppData\\Roaming\\Python\\Python313\\site-packages', 'C:\\Python313\\Lib\\site-packages', 'd:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent', 'd:/zyt/git_ln/elasticsearch-agent/', 'd:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent', 'd:/zyt/git_ln/elasticsearch-agent/', 'd:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent', 'd:/zyt/git_ln/elasticsearch-agent/', 'd:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent', 'd:/zyt/git_ln/elasticsearch-agent/']        
sys.path
['d:\\zyt\\git_ln\\elasticsearch-agent\\elasticsearch_agent\\agent\\test', 'C:\\Python313\\python313.zip', 'C:\\Python313\\DLLs', 'C:\\Python313\\Lib', 'C:\\Python313', 'C:\\Users\\zooos\\AppData\\Roaming\\Python\\Python313\\site-packages', 'C:\\Python313\\Lib\\site-packages', 'd:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent', 'd:/zyt/git_ln/elasticsearch-agent/', 'd:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent', 'd:/zyt/git_ln/elasticsearch-agent/', 'd:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent', 'd:/zyt/git_ln/elasticsearch-agent/', 'd:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent', 'd:/zyt/git_ln/elasticsearch-agent/', 'd:/zyt/git_ln/elasticsearch-agent/elasticsearch_agent', 'd:/zyt/git_ln/elasticsearch-agent/']
tools [{'type': 'function', 'function': {'name': 'elastic_list_indices', 'description': '输入是一个分隔符（例如逗号或换行符），输出是一个以分隔符分隔的索引列表。始终使用此工具来了解 Elasticsearch 集群中的索引。', 'parameters': {'description': '定义工具的输入数据模型。\n继承自 Pydantic 的 BaseModel，用于验证输入数据的结构和类型。', 'properties': {'separator': {'description': '用于分隔索引列表的分 隔符', 'title': 'Separator', 'type': 'string'}}, 'required': ['separator'], 'title': 'ListIndicesInput', 'type': 'object'}}}]        
INFO:root:请输入：：Can you please list all indices?
2025-10-08 22:27:34 - INFO - agent_factory:110 - 请输入：：Can you please list all indices?
INFO:root:

2025-10-08 22:27:34 - INFO - agent_factory:112 -

INFO:root:------------------------------------------------------------
2025-10-08 22:27:34 - INFO - agent_factory:124 - ------------------------------------------------------------
INFO:httpx:HTTP Request: POST https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions "HTTP/1.1 200 OK"
2025-10-08 22:27:35 - INFO - _client:1025 - HTTP Request: POST https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions "HTTP/1.1 200 OK"
INFO:root:
第1轮大模型输出信息：ChatCompletion(id='chatcmpl-3466e292-9dbc-4203-9eab-2826f37cfc2d', choices=[Choice(finish_reason='tool_calls', index=0, logprobs=None, message=ChatCompletionMessage(content='', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_4361065bca4e463d8c41be', function=Function(arguments='{"separator": ","}', name='elastic_list_indices'), type='function', index=0)]))], created=1759933657, model='qwen-plus', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=19, prompt_tokens=278, total_tokens=297, completion_tokens_details=None, prompt_tokens_details=PromptTokensDetails(audio_tokens=None, cached_tokens=0)))

2025-10-08 22:27:35 - INFO - agent_factory:129 -
第1轮大模型输出信息：ChatCompletion(id='chatcmpl-3466e292-9dbc-4203-9eab-2826f37cfc2d', choices=[Choice(finish_reason='tool_calls', index=0, logprobs=None, message=ChatCompletionMessage(content='', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_4361065bca4e463d8c41be', function=Function(arguments='{"separator": ","}', name='elastic_list_indices'), type='function', index=0)]))], created=1759933657, model='qwen-plus', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=19, prompt_tokens=278, total_tokens=297, completion_tokens_details=None, prompt_tokens_details=PromptTokensDetails(audio_tokens=None, cached_tokens=0)))

INFO:elastic_transport.transport:GET https://localhost:9200/_cat/indices?h=index&s=index [status:200 duration:0.062s]
2025-10-08 22:27:35 - INFO - _transport:351 - GET https://localhost:9200/_cat/indices?h=index&s=index [status:200 duration:0.062s]   
INFO:root:工具输出信息：employee,example_vector_index,people

2025-10-08 22:27:35 - INFO - agent_factory:153 - 工具输出信息：employee,example_vector_index,people

INFO:root:------------------------------------------------------------
2025-10-08 22:27:35 - INFO - agent_factory:154 - ------------------------------------------------------------
INFO:httpx:HTTP Request: POST https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions "HTTP/1.1 200 OK"
2025-10-08 22:27:36 - INFO - _client:1025 - HTTP Request: POST https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions "HTTP/1.1 200 OK"
INFO:root:第2轮大模型输出信息：ChatCompletionMessage(content='The indices in the Elasticsearch cluster are:\n\n- employee\n- example_vector_index\n- people', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None)

2025-10-08 22:27:36 - INFO - agent_factory:162 - 第2轮大模型输出信息：ChatCompletionMessage(content='The indices in the Elasticsearch cluster are:\n\n- employee\n- example_vector_index\n- people', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None)

INFO:root:最终答案：The indices in the Elasticsearch cluster are:

- employee
- example_vector_index
- people
2025-10-08 22:27:36 - INFO - agent_factory:163 - 最终答案：The indices in the Elasticsearch cluster are:

- employee
- example_vector_index
- people
INFO:elasticsearch_playground:Can you please list all indices?
2025-10-08 22:27:36 - INFO - agent_factory_test:125 - Can you please list all indices?
INFO:elasticsearch_playground:None
2025-10-08 22:27:36 - INFO - agent_factory_test:126 - None

D:\zyt\git_ln\elasticsearch-agent>