# class Parent1:
#     def __init__(self, value1, **kewords):
#         print('initializing Parent1')
#         super().__init__(**kewords)
#         self.value1 = value1
#
#
# class Parent2:
#     def __init__(self, value2, **kewords):
#         print('initializing Parent2')
#         super().__init__(**kewords)
#         self.value2 = value2
#
# class Child(Parent1,  Parent2):
#     def __init__(self, value1,value2):
#         print('initializing Child')
#         super().__init__(value1=value1,value2=value2)
#
#
# child = Child('value from Parent1','value from Parent2')
# print(child.  value1)
# print(child.value2)
import keyword


# class A:
#     def __init__(self, a,b,c,**kewords):
#         print('initializing A')
#         self.a = a
#         self.b = b
#         self.c = c
#         super().__init__(**kewords)
#
# class B:
#     def __init__(self, d,e,f):
#         print('initializing B')
#         self.d = d
#         self.e = e
#         self.f = f
#
#
# class C(A,B):
#     def __init__(self, a, b, c, d, e, f):
#      print('initializing C')
#      super().__init__(a=a, b=b, c=c, d=d, e=e, f=f)
#
#
# # print(C.__mro__)
# c = C(1,2,3,4,5,6)
#
# print(c.a)
# print(c.b)
# print(c.c)
#
# print(c.d)
# print(c.e)
# print(c.f)

class GrandParent:
    def __init__ (self):
        print ("Initializing GrandParent")

class Parent1 (GrandParent) :
    def __init__ (self):
        super().__init__ ()
        print ("Initializing Parentl")
class Parent2 (GrandParent):
    def __init__ (self):
        super().__init__()
        print ("Initializing Parent2")
class Child (Parent1, Parent2):
    def __init__(self):
        super().__init__()
# print(Child.__mro__)

Child()