class Expression:
    def __init__(self,func):
        self.func = func
    def __call__(self, value):
        return self.func(value)
    def __or__(self,other):
        return Expression(lambda x:other(self(x)))


def upper(x):
    return x.upper()

def lower(x):
    return x.lower()

def reviers(x):
    return x[::-1]

Upper = Expression(upper)
Lower = Expression(lower)
Reviers = Expression(reviers)

result = Expression(lambda x:x)|Upper|Reviers|Lower

print(result("hello world"))