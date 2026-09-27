list = [1,2,3,4,5,6,7,8,9]

print(sum(list))

for i in range(0,len(list)):
    print(list[i])


for i,value in enumerate(list,start=1):
    print(i,value)


del list[1]

print(list)


list2 = [[1,2,3],['a','b','c'],[7,8,9]]

for item in list2:
    print(item)


list6 = ["a","b","c"]
list7 = [1,2,3]

list8  = [(i,j) for i in list6 for j in list7]
print(list8)

list_str = ['http://www','baidu','com']

print('.'.join(list_str))