import json
from langchain_core.tools import Tool


def add(params: str) -> int:
    params = json.loads(params)
    a = params.get("a")
    b = params.get("b")
    return a + b


add_tool = Tool(name="add", description="add two numbers", func=add)

result = add_tool.invoke(json.dumps({"a": 1, "b": 2}))

print(result)