class X:
    b=2000
    def __init__(self):
        pass
    def display(self):
        print(X.a)
        print(X.b)
        print(self.c)

X.a=100
x1=X()
x1.c=62087118670
x2=X()
# del X.b
x1.display()
# x2.display()
del x1.c
# x1.display()