
def get_sum(sum1, sum2):
     assert isinstance(sum1, (int,float)) and isinstance(sum2, (int,float)) ,"类型必须为int或者float"
     return sum1 + sum2


print(get_sum(1, 1))