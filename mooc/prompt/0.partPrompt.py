# 部分提示词模版
from  langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template("把大象放进冰箱需要三步，第一步{first},第二步{second},第三步{third}")

first_prompt_template = prompt_template.partial(first="打开冰箱门")

second_prompt_template = first_prompt_template.partial(second="把大象放进去")

final_prompt = second_prompt_template.invoke({"third":"观赏冰箱门"})

print(final_prompt)


