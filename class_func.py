import types
# 添加实例方法
class Persion:
    def __init__(self,name):
        self.name = name

def eat(self):
    print(f"{self.name} eat!")

p1 = Persion("赵四")

p1.eat_func = types.MethodType(eat,p1)

p1.eat_func()

