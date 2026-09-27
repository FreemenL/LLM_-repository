import numpy as np
import matplotlib.pyplot as plt
#注意:新版本需要指定 matplotlib 使用 TkAgg 作为图形后端来渲染和显示图表
import matplotlib
import pandas as pd

matplotlib.use('TKAgg')#注意:中文显示需要额外设置字体
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


df = pd.read_csv('./data/2002-2026中美英软件技术专利走势.csv')
# 获取年份
x = df['year'].value_counts().index
print(np.array(x))
# 统计各个年份的数量

y = df.groupby("year")['数量'].sum()
print(y.values)

#创建数据
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([2, 4, 1, 5, 3])
#绘制折线图
plt.figure(figsize=(8,5))

plt.plot(x, y,color='blue')
#添加标题和标签
plt.title("折线图示例")
plt.xlabel("X轴")
plt.ylabel("Y轴")
#显示网格
plt.grid()
# 显示图表
plt.show()
