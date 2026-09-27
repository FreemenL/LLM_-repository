try:
   num_1 = int(input('请输入被除整数\n'))
   num_2 = int(input("请输入除数\n"))
   print(num_1/ num_2)

except ZeroDivisionError as e:
    print("除数为零异常",e)

except ValueError as e:
    print("值类型异常",e)

except Exception as e:
    print("捕获异常",e)

else:
    print("程序正常结束")

finally:
    print("程序结束")


