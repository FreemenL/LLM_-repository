from langchain_core.runnables import Runnable
from typing import Any, Dict


class DataValidator(Runnable):
    def invoke(self, input: Dict[str, Any], config: Any = None, **kwargs) -> Dict[str, Any]:
        # 验证输入数据
        if "name" not in input or "age" not in input:
            raise ValueError("输入数据缺少必要字段")
        return input


class AgeTransformer(Runnable):
    def invoke(self, input: Dict[str, Any], config: Any = None, **kwargs) -> Dict[str, Any]:
        # 转换年龄字段
        return {
            **input,
            "age_group": "青年" if input["age"] < 35 else "中年"
        }


age_pipeline = DataValidator() | AgeTransformer()

print(age_pipeline.get_graph().draw_ascii())

print(age_pipeline.invoke({"name": "Alice","age":46}))