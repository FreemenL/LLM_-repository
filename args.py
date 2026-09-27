# def func(name,**dict2):
#     print(name)
#     print(dict2)
#
# func("张三",age=12,gender="male")
from functools import reduce
from os import name

# def func(a,b,c):
#     print(a,b,c)
#
# tuple1 = (1,2,3)
#
# func(*tuple1)

# 强制使用位置参数和关键字参数，在形参列表中，/之前必须使用位置参数，*之后必须使用关键字参数，而/和*之间可以使用位置参数或关键字参数，但必须保持一致
# def func(a,b,/,c,d,*,e,f):
#     print(a,b,c,d,e,f)
#
# func(1,2,3,4,e=5,f=6)


# def func(num):
#     if num<=1:
#         return 1
#     else:
#         return num * func(num - 1)
#
# print(func(5))

# student_lists = [{"name": "zhangsan", "age": 55},{"name":'li4',"age":39},{"name":"li5","age":41}]
#
# print(sorted(student_lists,key=lambda x:x["age"],reverse=False))

list1 = [i for i in range(10)]
# print(list(filter(lambda x: x % 2 == 0, list1)))
print(list(map(lambda x: x ** 2, list1)))

# print(list(filter(lambda x: x % 2 == 0, list1)))

print(reduce(lambda x, y: x + y, list1))