from langchain_core.runnables import RunnableLambda

def add_one_with_types(x: int) -> str:
    return str(x + 1)

# 创建 RunnableLambda 并使用 with_types 显式声明输入输出类型
runnable = RunnableLambda(add_one_with_types).with_types(input_type=int, output_type=str)


print(runnable.input_schema.model_json_schema()) # Show inferred input schema
print(runnable.output_schema.model_json_schema()) # Show inferred output schema

# 调用
result = runnable.invoke (4)
print("\nResult:", type(result))