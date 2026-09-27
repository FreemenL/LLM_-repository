from langchain_core.runnables import RunnableLambda


def multiply(a, b):
    return a * b


def multiply_dict_waeper(inputs:dict):
    return multiply(inputs["a"], inputs["b"])

runnable_multiply = RunnableLambda(multiply_dict_waeper)

print(runnable_multiply.invoke({"a": 2, "b": 3}))


def multiply_tuple_waeper(inputs:tuple)->int:
    return multiply(inputs[0], inputs[1])

multiply_tuply_multiply = RunnableLambda(multiply_tuple_waeper)
print(multiply_tuply_multiply.invoke((3,3)))