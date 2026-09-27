# 组合提示词
from langchain_core.prompts import PromptTemplate
from langgraph.channels import topic

prompt_template = (
    PromptTemplate.from_template("给我讲一个笑话，关于{topic}")
    +",要非常简洁，10个字以内"
    +"\n\n用{language}讲述"
)

print(prompt_template.format(topic="猫",language="英语"))