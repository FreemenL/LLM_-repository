class MyClass:

    def __new__(cls, *args, **kwargs):
        print('__new__函数执行了')
        return super().__new__(cls)


    def __str__(self):
        return f"Myclass类的__str__函数{id(self)}"




p1 = MyClass()
print(p1)