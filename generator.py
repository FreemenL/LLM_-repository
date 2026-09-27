from collections.abc import Iterable,Iterator

gen_1 = (x for x in range(10))
print(gen_1)

for x in gen_1:
    print(x)


print(isinstance(gen_1,Iterable))
print(isinstance(gen_1,Iterator))
