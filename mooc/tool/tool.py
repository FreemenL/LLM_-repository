from langchain_core.tools import tool
# from pydantic import BaseModel, Field


# class CityModel(BaseModel):
#     city: str = Field(..., description="城市名称")


@tool(parse_docstring=True)
def get_weather(city: str) -> str:
    """获取天气信息

    Args:
        city (str): 城市名称

    Returns:
        str: 城市的天气信息
    """

    return "It's sunny in " + city


print(get_weather.name)
print(get_weather.description)
print(get_weather.args)
print(get_weather.args_schema.model_json_schema())