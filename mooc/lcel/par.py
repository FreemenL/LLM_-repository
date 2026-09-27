from langchain_core.runnables import RunnableLambda,RunnableParallel

def add_one(x: int) -> int:
    return x + 1

def mul_two(x: int) -> int:
    return x * 2

def mul_three(x: int) -> int:
    return x * 3

def add_two(input: dict)-> int:
    return input["mul_two"] + input["mul_three"]

runnable_1 = RunnableLambda(add_one)
runnable_2 = RunnableLambda(mul_two)
runnable_3 = RunnableLambda(mul_three)

runnable_4 = RunnableLambda(add_two)

pipeline = runnable_1 | {
    "mul_two": runnable_2,
    "mul_three": runnable_3
} | runnable_4

print(pipeline.get_graph().draw_ascii())

print(pipeline.invoke(1))