import re
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from typing import List, Dict,Any,Iterable
from langchain_core.output_parsers import BaseOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()


class TaskListOutputParser(BaseOutputParser[List[Dict[str, Any]]]):
    """自定义输出解析器，用于将 LLM 生成的文本解析为任务列表。

    该解析器期望输入文本格式为：
    1. [任务名称1] - [截止日期1] - [优先级1]
    2. [任务名称2] - [截止日期2] - [优先级2]
    ...
    """

    def parse(self, text: str) -> List[Dict[str, Any]]:
        """解析文本输出为任务列表。

        Args:
            text: LLM 生成的原始文本输出。

        Returns:
            结构化的任务列表，每个任务包含名称、截止日期和优先级。
        """
        tasks = []

        # 使用正则表达式匹配任务项
        task_pattern = r"^\s*\d+\.\s*\[(.*?)\]\s*-\s*\[(.*?)\]\s*-\s*\[(.*?)\]"

        for line in text.split('\n'):
            match = re.match(task_pattern, line)
            if match:
                name, deadline, priority = match.groups()
                tasks.append({
                    'name': name.strip(),
                    'deadline': deadline.strip(),
                    'priority': priority.strip()
                })

        return tasks

    def get_format_instructions(self) -> str:
        """返回格式说明，指导 LLM 如何格式化输出。"""
        return """
        请按照以下格式输出任务列表：

        1. [任务名称] - [截止日期] - [优先级]
        2. [任务名称] - [截止日期] - [优先级]
        3. [任务名称] - [截止日期] - [优先级]

        例如：
        1. [完成项目报告] - [2023-12-31] - [高]
        2. [准备演示文稿] - [2023-12-25] - [中]
        3. [回复邮件] - [2023-12-20] - [低]
        """


model = ChatOpenAI(
    model="deepseek-v4-pro",
    temperature=0
)


parser = TaskListOutputParser()

template = """
你是一个任务管理助手。请列出用户做下面事项时，需要计划3个任务。

事项: {text}

{format_instructions}
"""

prompt_template = PromptTemplate(
    template=template,
    input_variables=["text"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)


text = """
去北京旅游
"""

# 格式化提示
formatted_prompt = prompt_template.format_prompt(text=text)

# print(formatted_prompt)  # 打印生成的提示模板内容

response = model.invoke(formatted_prompt)

# print(type(response))
# print(response.content)

output = parser.invoke(response)
print("output", output)