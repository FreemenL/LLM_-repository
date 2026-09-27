# for i in range(0,10,2):
#     print(f"i={i}")
#
# string = 'helloworld'
# for i in string:
# #     print(f'i={i}')
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{i}x{j}={i*j}",end="\t")
#     print()

# 99乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}x{j}={i*j}",end="\t")
    print()