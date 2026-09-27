from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="deepseek-v4-pro",temperature=0)

examples = [
    {"input":"北京天气怎么样？","output":"北京市"},
    {"input":"南京属于江苏省","output":"南京市"},
    {"input":"武汉有什么好玩儿的地方","output":"武汉市"},
]


example_prompt = PromptTemplate(
    input_variables=["input","output"],
    template="输入：{input}\n输出：{output}",
)

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="请回答以下问题:",
    suffix="输入: {input}\n输出:",
    input_variables=["input"]
)

prompt = few_shot_prompt.format(input="烟花三月下扬州")

response = model.invoke(prompt)

print(response.content)