def createList():
   list = []
   for i in range(1000000):
       yield i
   return list

list = createList()

print(next(list))
print(next(list))
print(next(list))
print(next(list))
print(next(list))
print(next(list))


def gen_list():
    list = []
    for i in range(1000000):
        list.append(i)
    return list

list2 = gen_list()
print(list2)