from langchain_core.runnables import RunnableBranch
from langchain_core.tools import tool


@tool
def search(question: str):
    """使用搜索引擎回答问题"""
    return f"{question}->搜索结果..."


@tool
def wiki(question: str):
    """从维基百科获取相关信息"""
    return f"{question}->获取wiki结果..."


# 分支逻辑：根据问题类型选择工具
branch = RunnableBranch(
    (lambda x: "搜索" in x["question"].lower(), search),
    (lambda x: "获取" in x["question"].lower(), wiki),
    lambda x: "我不知道该怎么回答。"  # 默认回复
)

# 使用示例
result = branch.invoke({"question": "帮我获取法国首都"})
print(result)