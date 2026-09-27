from langchain_core.prompts import load_prompt

prompt_template = load_prompt("./prompt_template.json",encoding="utf-8")

prompt = prompt_template.invoke({"name":"小明","who":"猫"})

print(prompt)



