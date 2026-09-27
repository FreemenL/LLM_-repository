import re
from langchain_openai import ChatOpenAI
from typing import Any, Dict, Iterable, List
from langchain_core.output_parsers import BaseOutputParser
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()


class EntityExtractionParser(BaseOutputParser[Dict[str, List[str]]]):
    """自定义输出解析器，用于从文本中提取并分类实体。

    该解析器能够识别并分类以下实体类型：
    - 人物 (PERSON)
    - 地点 (LOCATION)
    - 事件 (EVENT)
    """

    def parse(self, text: str) -> Dict[str, List[str]]:
        """解析文本并提取分类实体。

        Args:
            text: LLM 生成的原始文本输出。

        Returns:
            结构化的实体字典，按类型分类。
        """
        entities = {
            "PERSON": [],
            "LOCATION": [],
            "EVENT": []
        }

        # 提取人物（支持逗号、顿号、空格分隔）
        person_pattern = r"(?:人物|姓名|人):\s*([^\n]+)"
        for match in re.finditer(person_pattern, text):
            persons = [p.strip() for p in re.split(r"[,，\s]+", match.group(1)) if p.strip()]
            entities["PERSON"].extend(persons)

        # 提取地点（支持逗号、顿号、空格分隔）
        location_pattern = r"(?:地点|位置|城市):\s*([^\n]+)"
        for match in re.finditer(location_pattern, text):
            locations = [l.strip() for l in re.split(r"[,，\s]+", match.group(1)) if l.strip()]
            entities["LOCATION"].extend(locations)

        # 提取事件（支持逗号、顿号、空格分隔）
        event_pattern = r"(?:事件|活动|发生):\s*([^\n]+)"
        for match in re.finditer(event_pattern, text):
            events = [e.strip() for e in re.split(r"[,，\s]+", match.group(1)) if e.strip()]
            entities["EVENT"].extend(events)
        return entities

    def get_format_instructions(self) -> str:
        """返回格式说明，指导 LLM 如何格式化输出。"""
        return """
        请按照以下格式输出信息：

        人物: [姓名1], [姓名2], [姓名3]
        地点: [位置1], [位置2], [位置3]
        事件: [事件1], [事件2], [事件3]

        例如：
        人物: 张三, 李四, 王五
        地点: 北京, 上海, 广州
        事件: 会议, 展览, 讲座
        """

model = ChatOpenAI(
    model="deepseek-v4-pro",
    temperature=0
)


parser = EntityExtractionParser()

template = """
你是一个信息提取助手。请从以下文本中提取人物、地点和事件：

文本: {text}

{format_instructions}
"""

prompt_template = PromptTemplate(
    template=template,
    input_variables=["text"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

text = """
2023年，特斯拉CEO埃隆·马斯克访问了中国上海的特斯拉超级工厂。
在那里，他参加了一个关于可持续能源的论坛，并宣布了新的投资计划。
同时，苹果公司CEO蒂姆·库克也在旧金山参加了全球开 发者大会。
"""

# 格式化提示
formatted_prompt = prompt_template.format_prompt(text=text)

# print(formatted_prompt)  # 打印生成的提示模板内容

response = model.invoke(formatted_prompt)
print("模型输出类型:", type(response))  # 打印模型的原始输出
print("模型输出:", response)  # 打印模型的原始输出

output = parser.invoke(response)
print(type(output))  # 打印解析后的对象类型
print(output)  # 打印解析后的对象内容