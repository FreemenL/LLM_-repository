# form random import randint
from random import randint

balance  = randint(0,100)
price = 50
print(balance)
if balance < price:
    print('余额不足，请充值')
print('欢迎下次光临')
