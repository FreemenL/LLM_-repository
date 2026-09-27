#组合提示词

from  langchain_core.prompts import PromptTemplate


full_template ="""
    {introduction}
    {example}
    {start}
"""

full_prompt_template = PromptTemplate.from_template(full_template)

# introduction
introduction_prompt_template = PromptTemplate.from_template("""你扮演{person}.""")

#example

example_template = """
    以下是一个互动示例
    Q:{example_q}
    A:{example_a}
"""
example_prompt_template = PromptTemplate.from_template(example_template)

#start
start_template = """
    以下是一个真实的互动！
    Q:{input}
    A:
"""

start_prompt_template  = PromptTemplate.from_template(start_template)

input_prompt = [
    ("introduction", introduction_prompt_template),
    ("example", example_prompt_template),
    ("start", start_prompt_template),
]

my_input = {
    "person":"马斯克",
    "example_q":"你喜欢的车是什么",
    "example_a":"Tesla",
    "input":"你喜欢的社交媒体网站是什么?"
}


for name, prompt in input_prompt:
    my_input[name] = prompt.invoke(my_input).to_string()

my_output = full_prompt_template.invoke(my_input)

print(my_output.text)