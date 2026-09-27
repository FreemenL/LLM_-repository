# mounth = int(input('请出入月份'))
#
# match mounth:
#     case 1 | 3 | 5|7 | 8|10 |12 :
#      print(f"{mounth}月有31天")
#     case 2:
#         print(f"{mounth}月有28天")
#     case 4 | 6| 9| 11 :
#         print(f"{mounth}月有30天")
#
# # 三目运算
import time_test

# num1 =10
# num2 =12
#
# max = num1 if num1 > num2 else num2
#
# print(f"{max=}")

number = 1

while number<=100:
    print("\r"+"#"*number,f"{number}%",end="")
    number+=1
    time.sleep(0.2)
print("下载成功")