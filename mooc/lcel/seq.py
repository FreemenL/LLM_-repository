from langchain_core.runnables import RunnableLambda,RunnableSequence


def add_one(x:int)->int:
    return x+1

def mul_two(x:int)->int:
    return x*2


add_one = RunnableLambda(func=add_one)
mul_two = RunnableLambda(func=mul_two)


sequence = RunnableSequence(first=add_one, last=mul_two)

print(sequence.get_graph().draw_ascii())

print(sequence.invoke(2))