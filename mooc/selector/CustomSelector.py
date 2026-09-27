from typing import Any, Dict,List

from dotenv import load_dotenv
from langchain_core.example_selectors import BaseExampleSelector
from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

class CustomExampleSelector(BaseExampleSelector):
    """医疗示例选择器"""
    def __init__(self, examples: List[Dict[str,str]]):
        self.examples = examples

    def add_example(self, example: dict[str, str]) -> None:
        self.examples.append(example)

    def select_examples(self, input_variables: Dict[str,Any]) -> List[Dict[str,Any]]:

          disease_name = input_variables.get("disease_name",None)
          if disease_name is None:
              return []

          selected_examples = [
              example for example in self.examples
              if disease_name.lower() in example["input"].lower()
          ]

          return selected_examples


examples = [
    {"input":"流感症状","output":"发烧，咳嗽，喉咙痛，身体酸痛"},
    {"input":"糖尿病治疗","output":"饮食控制，运动，药物"},
    {"input":"新冠肺炎症状","output":"发烧，咳嗽，疲劳，味觉或嗅觉丧失"},
    {"input":"糖尿病症状","output":"口渴，尿频，体重减轻"},
]

custom_example_selector = CustomExampleSelector(examples)

# selected_examples = custom_example_selector.select_examples({"disease_name":"新冠肺炎"})

# custom_example_selector.add_example({"input":"头晕症状","output":"头晕，眼睛模糊。"})

# selected_examples = custom_example_selector.select_examples({"disease_name":"头晕症状"})


example_prompt = PromptTemplate(
    input_variables=["input","output"],
    template="输入:{input}\n输出:{output}",
)
dynamic_prompt = FewShotPromptTemplate(
    example_selector=custom_example_selector,
    example_prompt=example_prompt,
    prefix="根据描述确定病情",
    suffix="输入{disease_name}\n输出",
    input_variables=["disease_name"],
)


prompt  = dynamic_prompt.format(disease_name="糖尿病")

# print(prompt)
llm = ChatOpenAI(model="deepseek-v4-pro",temperature=0)

response = llm.invoke(prompt)
print(response.content)