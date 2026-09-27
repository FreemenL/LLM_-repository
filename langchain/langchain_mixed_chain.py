from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

llm = ChatOpenAI(model="gpt-5.5")

parser = StrOutputParser()

prompt_template_1 = PromptTemplate.from_template("正面评价一下{topic}这个问题")
prompt_template_2 = PromptTemplate.from_template("负面评价一下{topic}这个问题")

prompt_template_sum = PromptTemplate.from_template("根据这两个分析:{view_1}和{view_2},给出一个汇总的结果")

chain_1 = prompt_template_1 | llm| parser
chain_2 = prompt_template_2 | llm| parser
chain_sum = prompt_template_sum | llm | parser

map_chain = {
    "view_1":chain_1,
    "view_2":chain_2
} |  chain_sum

responses = map_chain.invoke({"topic":"加班"})
print(responses)
