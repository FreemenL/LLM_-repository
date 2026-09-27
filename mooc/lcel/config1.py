from langchain_core.runnables import RunnableLambda

def add_one(x: int, config: dict) -> int:
    print(f"add_one:{config}")

    return x + 1

def double(x: int, config: dict) -> int:
    print(f"double:{config}")

    return x * 2


pipline = (RunnableLambda(add_one).with_config({
    "timeout": 5,
    "userId": "user-123",
    "tags": ["math", "demo"],
    "metadata": {"source": "user_input"}
    })
| RunnableLambda(double)
)

print(pipline.invoke(1))