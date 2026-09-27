import numpy as np


arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print('原始数组',arr)

# print(arr[0,0]) # 第一个元素
# print(arr[-1]) # 最后一行
# print(arr[:,1]) # 所有行的第二列


# print(arr[:2]) # 前两行
# print(arr[:2,:2]) # 前两行 前两列
# print(arr[::2,::2]) #行和列都隔一个取一个


print(arr.shape)
print(arr.ndim)
