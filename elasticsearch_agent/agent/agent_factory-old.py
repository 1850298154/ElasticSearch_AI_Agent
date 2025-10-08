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

# 定义一个工具列表，包含多个自定义工具实例
tools = [
    ListIndicesTool(),  # 列出所有索引的工具实例
    IndexShowDataTool(),  # 显示索引数据的工具实例
    IndexDetailsTool(),  # 显示索引详细信息的工具实例
    create_search_tool(),  # 创建搜索工具的实例
]

# 定义一个工厂函数，用于创建并返回一个 AgentExecutor 实例
def agent_factory() -> AgentExecutor:
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