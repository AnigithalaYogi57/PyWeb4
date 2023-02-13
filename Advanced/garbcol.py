class X:
    def __init__(self):
        print("i am in constructor")

    def __del__(self):
        print("i am in destructor")


x1=X()
x2=x1
x3=x2

del x1
del x2
del x3
