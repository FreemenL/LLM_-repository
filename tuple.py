tuple1 = ([1,2,3],1,22,33,444)

for item in tuple1:
    print(item)

for item,value in enumerate(tuple1):
    print(item,value)

tuple1[0].append(5)

print(tuple1)

set2 = {1,2,3}

print(type(set2))