from typing import Optional

from dotenv import load_dotenv
from langchain_community.tools import TavilySearchResults
from langchain_core.messages import ToolMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()


@tool("get_weather", parse_docstring=True)
def weather_tool(location: str, date: Optional[str] = None) -> str:
    """获取指定位置的天气

    Args:
        location: 地点
        date: 日期，比如今天、明天或具体日期
    """
    date_text = date or "当前"
    return f"{date_text}{location}的天气晴朗，温度25°C"


@tool("tavily_search", parse_docstring=True)
def search_tool(query: str) -> str:
    """用于查询搜索引擎的工具

    Args:
        query: 查询内容
    """
    search = TavilySearchResults(
        max_results=1,
        include_answer=True,
        include_raw_content=True,
        include_images=False,
        include_image_descriptions=False,
    )

    return search.run(query)


llm = ChatOpenAI(model="deepseek-v4-pro", temperature=0)

tools = [search_tool, weather_tool]
tools_by_name = {item.name: item for item in tools}
llm_with_tools = llm.bind_tools(tools)

prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个有用的AI助手。遇到天气问题时必须调用 get_weather 工具；"
            "遇到需要搜索的问题时调用 tavily_search 工具。工具返回后，要基于工具结果回答用户。",
        ),
        ("human", "{question}"),
    ]
)


def ask_with_tools(question: str) -> str:
    messages = prompt_template.invoke({"question": question}).to_messages()
    ai_message = llm_with_tools.invoke(messages)

    if not ai_message.tool_calls:
        return ai_message.content

    messages.append(ai_message)
    for tool_call in ai_message.tool_calls:
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        selected_tool = tools_by_name[tool_name]
        tool_response = selected_tool.invoke(tool_args)

        print(f"调用工具: {tool_name}, 参数: {tool_args}")
        print(f"工具返回: {tool_response}")

        messages.append(
            ToolMessage(
                content=str(tool_response),
                tool_call_id=tool_call["id"],
            )
        )

    final_message = llm.invoke(messages)
    return final_message.content


if __name__ == "__main__":
    result = ask_with_tools("明天北京天气如何")
    print(result)
    print(type(result))
