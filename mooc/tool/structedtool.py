# 银行账户查询场景下，如何定义一个多参数工具。
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field
from typing import Optional


class BankAccountQuery(BaseModel):
    account_id: str = Field(description="用户的银行账号")
    start_date: Optional[str] = Field(default=None, description="查询开始日期，格式YYYY-MM-DD")
    end_date: Optional[str] = Field(default=None, description="查询结束日期，格式YYYY-MM-DD")
    query_type: str = Field(
        default="balance",
        enum=["balance", "transactions", "interest_rate"],
        description="查询类型：余额查询、交易记录或利率查询"
    )


def query_bank_account(
        account_id: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        query_type: str = "balance"
) -> str:
    """查询银行账户信息"""
    # 这里通常会调用实际的银行API
    # 为了示例，我们只返回模拟数据

    if query_type == "balance":
        return f"账户 {account_id} 当前余额为: ¥10,000.00"
    elif query_type == "transactions":
        if start_date and end_date:
            return f"账户 {account_id} 在 {start_date} 到 {end_date} 之间有5笔交易"
        else:
            return f"账户 {account_id} 最近有9笔交易"
    elif query_type == "interest_rate":
        return f"账户 {account_id} 的当前利率为 1.5%"
    else:
        return "不支持的查询类型"


bank_tool = StructuredTool.from_function(
    func=query_bank_account,
    name="query_bank_account",
    description="查询银行账户信息的工具，可以查询余额、交易记录或利率",
    args_schema=BankAccountQuery
)

print(bank_tool.args_schema.model_json_schema())

result = bank_tool.invoke(
    {
        "account_id": "123456",
        "start_date": "2023-01-01",
        "end_date": "2023-01-31",
        "query_type": "transactions"
    }
)

print(result)