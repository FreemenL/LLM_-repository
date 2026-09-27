# 部分提示词模版
from langchain_core.prompts import PromptTemplate


prompt = PromptTemplate(
    template="把大象放进冰箱分三步：\n第一步：{first},第二步：{second},第三步：{third}",
    input_variables=["second","third"],
    partial_variables={"first":"打开冰箱门"},
)

partial_prompt = prompt.partial(second="把大象放进去")

print(partial_prompt.format(third="关上冰箱门"))