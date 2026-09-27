class Person:
    def __init__(self):
        self.name = "zhangsan"
        self.age = 12
        self.gender = "male"
        self.email = "xiajiang818@gmail.com"
    def eat(self):
        print("eat dinner")
    def sleep(self):
        print("sleep 3 ms")


p = Person()
p.eat()
print(p.name)
print(p.age)
print(p.gender)
print(p.email)