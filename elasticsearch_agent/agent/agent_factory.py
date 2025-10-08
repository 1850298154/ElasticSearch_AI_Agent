# 从 langchain 库中导入初始化 agent 的方法
from langchain.agents.initialize import initialize_agent
# 从 langchain 库中导入 AgentExecutor 类，用于执行 agent
from langchain.agents.agent import AgentExecutor
# 从 langchain 库中导入 AgentType 枚举类，用于定义 agent 的类型
from langchain.agents.agent_types import AgentType
# 从 langchain.prompts.chat 模块中导入 SystemMessage 类，用于定义系统消息
# from langchain.prompts.chat import SystemMessage
from langchain.schema import SystemMessage

# 从 elasticsearch_agent.config 模块中导入配置对象 cfg
from elasticsearch_agent.config import cfg
# 从 elasticsearch_agent.tools 模块中导入自定义工具类
from elasticsearch_agent.tools.list_indices_tool import ListIndicesTool  # 列出所有索引的工具
from elasticsearch_agent.tools.index_data_tool import IndexShowDataTool  # 显示索引数据的工具
from elasticsearch_agent.tools.index_details_tool import IndexDetailsTool  # 显示索引详细信息的工具
from elasticsearch_agent.tools.index_search_tool import create_search_tool  # 创建搜索工具的函数

import traceback
import json

import logging
from llmLog import init_logging
init_logging()

import time
from openai import OpenAI
from elasticsearch_agent.secret import model_api_key

from langchain.tools.base import BaseTool

def trans(tools: list[BaseTool]) -> list:
    tools = [{
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description,
            # 因为获取当前时间无需输入参数，因此pa,ameters为空字典
            "parameters": tool.args_schema.schema(),
        },
    } for tool in tools]
    return tools

list_indices_tool=ListIndicesTool()
index_show_data_tool=IndexShowDataTool()
index_details_tool=IndexDetailsTool()
search_tool=create_search_tool()
# 定义一个工具列表，包含多个自定义工具实例
tools = [
    list_indices_tool,
    index_show_data_tool,
    index_details_tool,
    search_tool,
]
tools = trans(tools)
print('tools', tools)


client = OpenAI(
    api_key=model_api_key,    
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope SDK的base_url
)

# 封装模型响应函数
def get_response(messages):
    time_start = time.time()
    completion = client.chat.completions.create(
        model="qwen-plus",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        # https://help.aliyun.com/zh/model-studio/models
        messages=messages,
        tools=tools,
    )
    time_end = time.time()
    diff_time = time_end - time_start
    # store_observation_info(
    #     completion=completion,
    #     input_data=messages,
    #     execution_time=diff_time,
    # )
    return completion

def call_tools_safely(tool_info, assistant_output):
    def call_tools(tool_info, assistant_output):

        if assistant_output.tool_calls[0].function.name == list_indices_tool.name:
            # 提取位置参数信息
            arguments = json.loads(assistant_output.tool_calls[0].function.arguments)
            tool_info["content"] = list_indices_tool.run(arguments)
        elif assistant_output.tool_calls[0].function.name == index_show_data_tool.name:
            # 提取位置参数信息
            arguments = json.loads(assistant_output.tool_calls[0].function.arguments)
            tool_info["content"] = index_show_data_tool.run(arguments)
        elif assistant_output.tool_calls[0].function.name == index_details_tool.name:
            # 提取位置参数信息
            arguments = json.loads(assistant_output.tool_calls[0].function.arguments)
            tool_info["content"] = index_details_tool.run(arguments)
        elif assistant_output.tool_calls[0].function.name == search_tool.name:
            # 提取位置参数信息
            arguments = json.loads(assistant_output.tool_calls[0].function.arguments)
            tool_info["content"] = search_tool.run(arguments)
    
    
    try:
        call_tools(tool_info, assistant_output)
    except Exception as e:
        # 获取完整的错误信息（包括堆栈）
        error_msg = traceback.format_exc()
        
        # 保存到文件
        with open("error_log.txt", "a") as f:
            f.write(f"错误发生时间: ...\n")  # 可以添加时间戳
            f.write(error_msg)
            f.write("\n" + "="*50 + "\n")
        
        # 或者使用 logging 模块
        logging.error("函数调用失败", exc_info=True)



def call_with_messages(react_system_prompt,user_input):
    user_hint = "请输入："
    # user_input = input(user_hint)
    logging.info(f"{user_hint}：{user_input}")

    logging.info("\n")
    messages = [
        {
            "content": react_system_prompt,
            "role": "system",
        },
        {
            "content": user_input,

            "role": "user",
        }
    ]
    logging.info("-" * 60)
    # 模型的第一轮调用
    i = 1
    first_response = get_response(messages)
    assistant_output = first_response.choices[0].message
    logging.info(f"\n第{i}轮大模型输出信息：{first_response}\n")
    if assistant_output.content is None:
        assistant_output.content = ""
    messages.append(assistant_output)
    # 如果不需要调用工具，则直接返回最终答案
    if (
        assistant_output.tool_calls == None
    ):  # 如果模型判断无需调用工具，则将assistant的回复直接打印出来，无需进行模型的第二轮调用
        logging.info(f"无需调用工具，我可以直接回复：{assistant_output.content}")
        return
    # 如果需要调用工具，则进行模型的多轮调用，直到模型判断无需调用工具
    while assistant_output.tool_calls != None:
        # 如果判断需要调用查询天气工具，则运行查询天气工具
        tool_info = {
            "content": "",
            "role": "tool",
            "tool_call_id": assistant_output.tool_calls[0].id,
            "tool_call_name": assistant_output.tool_calls[0].function.name,
            "tool_call_arguments": assistant_output.tool_calls[0].function.arguments,
        }

        call_tools_safely(tool_info, assistant_output)

        tool_output = tool_info["content"]
        logging.info(f"工具输出信息：{tool_output}\n")
        logging.info("-" * 60)
        messages.append(tool_info)
        loop_response = get_response(messages)
        assistant_output = loop_response.choices[0].message
        if assistant_output.content is None:
            assistant_output.content = ""
        messages.append(assistant_output)
        i += 1
        logging.info(f"第{i}轮大模型输出信息：{assistant_output}\n")
    logging.info(f"最终答案：{assistant_output.content}")



# 定义一个工厂函数，用于创建并返回一个 AgentExecutor 实例
def agent_factory():
    # 从 langchain.agents.openai_functions_agent.base 模块中导入 OpenAIFunctionsAgent 类
    from langchain.agents.openai_functions_agent.base import OpenAIFunctionsAgent

    # 定义一个空列表，用于存储 agent 的标签
    tags_ = []
    # 定义 agent 的类型为 OPENAI_FUNCTIONS， 该类型是用于调用 OpenAI 函数的 agent
    agent = AgentType.OPENAI_FUNCTIONS
    # 如果 agent 是 AgentType 的实例，则将其值添加到标签列表中
    tags_.append(agent.value if isinstance(agent, AgentType) else agent) # 添加 agent 类型标签， # OPENAI_FUNCTIONS
    
    # 使用 OpenAIFunctionsAgent 的 from_llm_and_tools 方法创建 agent 对象
    agent_obj = OpenAIFunctionsAgent.from_llm_and_tools(
        cfg.llm,  # 使用配置中的 LLM（语言模型）
        tools,  # 使用定义的工具列表
        system_message=SystemMessage(content="You are a helpful AI ElasticSearch Expert Assistant")  
        # 定义系统消息，内容为“你是一个有帮助的 AI ElasticSearch 专家助手”
    )
    
    # 返回一个 AgentExecutor 实例，通过 from_agent_and_tools 方法创建
    return AgentExecutor.from_agent_and_tools(
        agent=agent_obj,  # 使用创建的 agent 对象
        tools=tools,  # 使用工具列表
        tags=tags_,  # 使用定义的标签列表
        verbose=cfg.langchain_verbose  # 是否启用详细日志，由配置中的 langchain_verbose 决定
    )

# 如果当前脚本是主程序入口
if __name__ == "__main__":
    # 调用 agent_factory 函数，创建一个 agent_executor 实例
    agent_executor = agent_factory()
    # 获取 agent 的 prompt（提示信息）
    prompt = agent_executor.agent.prompt
    # 打印 prompt 的内容
    print(prompt)
    # 打印 prompt 的类型
    print(type(agent_executor.agent.prompt))