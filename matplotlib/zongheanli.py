# 加载数据
import pandas as pd
import matplotlib.pyplot as plt
#注意:新版本需要指定 matplotlib 使用 TkAgg 作为图形后端来渲染和显示图表
import matplotlib

matplotlib.use('TKAgg')


plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Hiragino Sans GB',
                                   'Arial Unicode MS', 'SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./data/1960-2019全球GDP数据.csv', encoding='gbk')


# 处理缺失值
# inplace=True 原地修改
df.dropna(inplace=True) # 在自身修改

china = df[df["country"]=="中国"]
usa = df[df["country"]=="美国"]
jp = df[df["country"]=="日本"]


# print(china)


china.set_index("year",inplace=True)
usa.set_index("year",inplace=True)
jp.set_index("year",inplace=True)



# 设置折线图的标题
plt.title("1960-2019全球GDP数据折线图")


plt.plot(china.index, china["GDP"], label="中国", color="red")
plt.plot(usa.index, usa["GDP"], label="美国", color="blue")
plt.plot(jp.index, jp["GDP"], label="日本", color="green")

# 显示图例:读取每条折线的 label,在图上标注出来
plt.legend()
# 显示网格线:便于读数,横向对比数值大小
plt.grid()
# 弹出窗口显示图表,并阻塞程序运行,直到关闭窗口后脚本才结束
plt.show()


