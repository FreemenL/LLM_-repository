# 数据清洗 处理缺失值
import pandas as pd

df = pd.read_csv('data/清洗数据.csv',sep=',')

print("原始数据，包含缺失值")
print(df)

print("缺失值统计")
print(df.isnull().sum())

print(df.notnull().sum())
df.info()




print(df.dropna())
print(df.dropna(how='all'))


print(df.fillna(0))
print(df.fillna(df.mean()))

