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
print(d.a)
d.firstmethod()
d.secondmethod()
print("end")

l=[1,2,3]
l.append(4)