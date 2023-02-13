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
