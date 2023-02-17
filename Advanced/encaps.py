'''
print("================method overloading=============")
class X:
    def m1(self,p):
        print("1st defined method")
    def m1(self,p,q):
        print("2nd defined method")
    def m1(self,p,q,r):
        print("last defined method")

x1=X()
x1.m1(1,2,3)
'''
'''
print("================method overriding=============")

class X:
    def m1(self):
        print("This is m1 of X")

class Y(X):
    def m1(self):
        print("This is m1 of Y")
        super().m1()

# y1=Y()
# y1.m1()

class X:
	def __init__(self):
		self.a=1000
		self.b=2000

class Y(X):
	def __init__(self):
		super().__init__()
		self.c=3000
		self.d=4000

	def display(self):
		print(self.a)
		print(self.b)
		print(self.c)
		print(self.d)


y1=Y()
y1.display()
'''
print("================Abstraction=============")

class X:
    __a=1000
    def m1(self):
        print(X.__a)
class Y(X):
    def m2(self):
        print("in m2 of Y")
        # print(X.__a)
# print(X.__a)
# x1=X()
# x1.m1()
y1=Y()
y1.m2()
print("accessing outside:",X._X__a)