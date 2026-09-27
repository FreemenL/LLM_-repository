def get_sum(num1, num2):
    if isinstance(num1, (int,float)) and isinstance(num2, (int,float)):
        return num1 + num2;
    else:
        raise TypeError("参数类型错误，必须为int或float")



try:
    print(get_sum("1", 2))
except TypeError as e:
    print(e)


print("程序结束")