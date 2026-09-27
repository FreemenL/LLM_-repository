# 创建集合
import copy

# set1 = {1,2,3,4,1,2,3,9}
# set2 = set()
# set3 = set({1,2,3})
#
# print(set1,type(set1))
# print(set2,type(set2))
# print(set3,type(set3))

# for i in set1:
#     print(i,end="\t")

set1 = {1,2,3,4,5,6,7,8,9}
set2 = {1,2,3,4,5,6,7,8,9,10}
# set1.update([1000,2000])
# set2 = set1.union({1000,2000})
# set1.remove(99)
# set1.pop()
# set1.clear()
# print(set2.difference(set1))
# difference_update 作用于原集合
# set1.difference_update(set2)
# 获取交集 作用于原集合  {1, 2, 3, 4, 5, 6, 7, 8, 9}
# set1.intersection_update(set2)
# 获取交集
# print(set1|set2)
# print(set1.issubset(set2))
# print(copy.deepcopy(set1))


dict1 = {"name":"张三","age":12,"gender":"male"}
dict2 = dict({"name":"张三","age":12,"gender":"male"})
print("name" in dict1)

for key in dict1.keys():
    print(key)

for value in dict1.values():
    print(value)


