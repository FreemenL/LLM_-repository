from datetime import datetime

from pyasn1.codec.ber.decoder import decode

from utils import chat_with_LLM
def get_current_date():
    return f"{datetime.now().month}/月"

def search_holidays(month):
    holidays = {
        "1月": ["元旦：1月1日"],
        "2月": ["春节：1月28日-2月3日"],
        "3月": [],
        "4月": ["清明节：4月4日-6日"],
        "5月": ["劳动节：5月1日-5日", "端午节：5月31日-6月2日"],
        "6月": ['儿童节：6月1日'],
        "7月": [],
        "8月": [],
        "9月": ["中秋节：9月25日"],
        "10月": ["中秋节：10月6日-8日", "国庆节：10月1日-7日"],
        "11月": [],
        "12月": ["元旦：12月31日"]  # 实际元旦在1月，这里仅作示例
    }
    return holidays.get(month,"没有这个月份")


TOOLS = {
    "get_current_date": get_current_date,
    "search_holidays": search_holidays,
}

def docode_response(response):
    lines = response.split("\n")
    thought = lines[0].strip()[len("Thought:"):].strip()
    action = lines[1].strip()[len(" Action:"):].strip()
    action_input = lines[2].strip()[len("Action Input:"):].strip()
    return thought,action,action_input

"""
User Question
→ LLM → Thought
→ LLM → Action + Action Input
→ Python代码解析Action，调用工具 → Observation
→ 把Observation追加到上下文
→ 循环直到输出 Final Answer
"""
def react(question):
    max_setp = 6
    setps = []
    for item in range(max_setp):
        context = '\n'.join(setps)
        prompt = f"""
            你是一个使用ReAct范式的智能代理，必须严格按以下格式输出：
            一个字都不能错，不能多加内容，必须按照以下格式输出：
            Thought: <你的思考>
            Action: <要执行的动作，从 [get_current_date, search_holidays] 中选择，当知道结果后返回: Action:Final Answer>
            Action Input: <如果Action是动作名称，则填写该工具的输入参数；如果Action是Final Answer，则填写最终答案>
            当前上下文：
            {context}
            问题：{question}
            【工具说明】
            - get_current_date
              作用：获取月份
              传入参数：无
              返回结果：月份，如10月
            - search_holidays
              作用：查询节假日
              传入参数：月份，如2月
              返回结果：节假日信息，如 1月3日~1月9日 春节
            
            【正确示例】
            - 示例1（调用工具）：
              Thought: 要回答本月有哪些法定假日，首先需要获取当前月份，才能针对性查询假期。
              Action: get_current_date
              Action Input: ''
            - 示例2（输出最终答案）：
              Thought: 已通过查询得知当前月份是2024年10月，该月的法定假日是10月1日-7日（国庆节），可以给出最终答案。
              Action: Final Answer
              Action Input: 2024年10月的法定节假日是国庆节，放假时间为10月1日至7日     
        """
        print(f"第{item}次调用模型：上下文是：\n{context}")
        message = [{"role": "user", "content": prompt}]
        response = chat_with_LLM(message)
        print(response)
        thought , action ,action_input = docode_response(response)
        print(f"解析模型内容：{thought}\n{action}\n{action_input}")
        if action == "Final Answer":
            print(f"最终回答：{action_input}")
            return action_input

        # 检查记录模型的回答。当做下次的上下文。
        setps.append(f'Thought:{thought}')
        setps.append(f'action:{action}')
        setps.append(f'Action Input:{action_input}')

        if action in TOOLS:
            if action == "get_current_date":
                res_data = TOOLS[action]()
            else:
                res_data = TOOLS[action](action_input)
            setps.append(f"Observation: {res_data}")
        else:
            print(f"Error:模型返回方法错误：{action}")
            setps.append(f"Error:模型返回方法错误：{action}")


if __name__ == '__main__':
    react('这个月的节假日有哪些？')





