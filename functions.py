print("begin")

def testfunc(): #function declaration
    """This is a testfunc to test the doc string"""
    print("i am in testfunc") #function body

testfunc() #function calling
c=1
d=2
print(c+d)
testfunc()
testfunc()
testfunc()
help(testfunc)
print("end")
print("----------------parameters---------------")

def add(a,b):
    '''this function is used to find the addition of two number'''
    c=a+b
    print(c)

add(1,2)
add(100,200)

def add1(a=10,b=20):
    c=a+b
    print(c)

add1()
add1(20)
add1(20,30)

def add2(a,b,c=30):
    print(a+b+c)

add2(10,20)
add2(10,20,40)
# add2(10)
# add2(20,30,40,50)
