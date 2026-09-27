# 长度选择器
from dotenv import load_dotenv
from langchain_core.example_selectors import LengthBasedExampleSelector
from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate
from langchain_openai import ChatOpenAI

examples = [
    {"input":"快乐","output":"悲伤"},
    {"input": "高", "output": "矮"},
    {"input": "精力充沛", "output": "昏昏欲睡"},
    {"input": "阳光", "output": "阴暗"},
    {"input": "喧哗", "output": "安静"}
]


example_prompt = PromptTemplate(
    input_variables=["input","output"],
    template = "input:{input}\noutput:{output}"
)

example_selector= LengthBasedExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    max_length=30,
    get_text_length= lambda x: len(x),
)

dynamic_prompt = FewShotPromptTemplate(
    example_selector = example_selector,
    example_prompt = example_prompt,
    suffix = "Input:{input}\nOutput:",
    input_variables=["input"]
)

short_question = "大"

prompt1 = dynamic_prompt.format(input=short_question)

print(prompt1)

load_dotenv()
# llm = ChatOpenAI(model="deepseek-v4-pro",temperature=0)
#
# response = llm.invoke(prompt1)

# print(response.content)

# print('example_selector.example_text_lengths',example_selector.example_text_lengths)
print('short_question 使用的示例数量',len(example_selector.select_examples({input:short_question})))
