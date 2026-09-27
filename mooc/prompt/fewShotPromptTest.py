from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="deepseek-v4-pro",temperature=0)

examples = [
    {"input":"2🐦2","output":"4"},
    {"input":"2🐦3","output":"5"},
    {"input":"4🐦5","output":"9"},
]


example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human","{input}"),
        ("ai","{output}"),
    ]
)

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)

final_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是个数学奇才"),
        few_shot_prompt,
        ("human","{input}"),
    ]
)

s = final_prompt_template.invoke({"input":"2🐦9"}).to_string()

# print(s)

response = model.invoke(s)
print(response.content)


