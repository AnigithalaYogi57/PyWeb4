'''
print("-----------------Has a releationship----------------------")

class X:
    a=100
    def __init__(self):
        print("X class constructor")
        self.b=200

    def m1(self):
        print('i am in m1 of X')
class Y:
    c=300
    def __init__(self):
        print("Y class constructor")
        self.d=400

    def m2(self):
        print('i am in m2 of Y')

    def m3(self):
        print('i am in m3 of Y')
        print(X.a)
        x1=X()
        x1.m1()
        print(Y.c)
        print(self.d)
        self.m2()

y1=Y()
y1.m3()
'''
'''
print("-----------------is a releationship----------------------")
class X():
    a=100
    def m1(self):
        print('i am in m1 of X')

class Y(X):
    c=300
    def __init__(self):
        print("Y class constructor")
        self.d=400

    def m2(self):
        print('i am in m2 of Y')

    def m3(self):
        print(Y.a)
        print(Y.c)
        print("i am in m3 of Y")
        self.m2() # Y.m2(self)
        self.m1()


y1=Y()
y1.m3()
y1.m1()
'''
'''
class A(object):
    def m1(self):
        print('in m1 of A')
class B(A):
    def m2(self):
        print('in m2 of B')
class C(A):

    def m3(self):
        print('in m3 of C')

b1=B()
b1.m1()
b1.m2()

c1=C()
c1.m3()
c1.m1()
'''
'''
class A(object):
    def m1(self):
        print('in m1 of A')
class B(object):
    def m2(self):
        print('in m2 of B')
class C(A,B):
    def m3(self):
        print('in m3 of C')

c1=C()
c1.m1()
c1.m2()
c1.m3()

class X(object): # X(Z) cyclic inheritance is not supported
    pass

class Y(X):
    pass

class Z(Y):
    pass

'''