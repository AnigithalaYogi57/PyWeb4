'''
print("begin")

class Demo:
    a=10
    b=20
    def firstmethod(self):
        print("this is first method")
    def secondmethod(self):
        print("this is second method")
d=Demo() #d is holding an original(direct) address so, d is pointer variable
self = d #self is holding same address(indirect address) so self is a referance variable
x=self # x is also a referance variable
print(d)
print(d.a)
d.firstmethod()
d.secondmethod()
print("end")

l=[1,2,3]
l.append(4)
'''

'''
print("-----------static variables------------")
class Student:
    school_name = "lchs"
    def m1(self):
        print("inside class",Student.school_name)
        print("i am in m1 of X")
        print(self.school_name)

s1=Student()
print("outside class",Student.school_name)
print(s1.school_name)
s1.m1()
s2=Student()
print(s2.school_name)
s3=Student()
print(s3.school_name)

'''
'''
class X:
    a=1000
    b=2000

    def display(self):
        print(X.a)
        print(X.b)

    def modify(self):
        X.a=3000
        X.b=4000

x1=X()
x1.display()
x1.modify()
x1.display()
x2=X()
x2.display()
'''
'''
print("-----------Non-static variables------------")
class X:
    a=1000
    b=2000

    def initialize(self):
        self.p=5000
        self.q=6000

    def show(self):
        print("non-static",self.p)
        print("non-static",self.q)
        print('class var',X.a)
        print('class var', X.b)

    def modify(self):
        X.a=3000
        X.b=4000
        self.p=7000
        self.q=8000
print("x1 object")
x1=X()
x1.initialize()
x1.show()
x1.modify()
x1.show()
print("x2 object")
x2=X()
x2.modify()
x2.show()
'''

print("-------constructor---------------")

class X:
    a=100
    b=200
    def __init__(self):
        print("This constuctor is executed when object is created")
        self.p=4000
        self.q=5000

    def display(self):
        print(self.p)
        print(self.q)

    def modify(self):
        i='yogi' #local variable
        self.p=6000
        self.q=7000
        print(i)
print("outside static",X.a)
x1=X()
print("outside nonstatic",x1.p)
x2=X()
x3=X()
x1.display()
x2.modify()
x3.display()
