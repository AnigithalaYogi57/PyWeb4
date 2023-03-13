
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
'''
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

print("====================Arguments===================")
def greet(name,msg):
    print("Hello",name,msg)

greet('yogi', 'good morning!')
greet("goodmorning!",'yogi')

def greet(name,msg):
    print("Hello",name,msg)

greet(name='yogi', msg='good morning!')
greet(msg="good morning!",name='yogi')
greet("good morning",msg="yogi")
print("====================Orbitary parameters===================")

def add(*a):
    print(a)
    print(type(a))
    print("total=",sum(a))

add(1,2,4,5,6)

def add10(a,*b):
    print(a)
    print(b)
    print(type(a))
    print(type(b))

add10(1,2,4,5,6)

def add11(*a,b=10):
    print(a)
    print(b)
    print(type(a))
    print(type(b))

add11(1,2,4,5,6,b=9)


def add12(*a,**k):
    print(a)
    print(k)
    print(type(a))
    print(type(k))

add12(1,2,4,5,6,b=9,c=11)


def add12(x,y,*args,**kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)
    print(type(args))
    print(type(kwargs))

add12(1,2,4,5,6,b=9,c=11)
'''

print("================return statement===============")

def test(a,b):
    c=a+b
    return c
    print("This statement will not print")

result = test(1,2)

print(result)

test(1,3)

def absolute(a):
    if a<0:
        return -a
    else:
        return a
    print("end of absolute")
x=absolute(-5)
print(x)
y=absolute(15)
print(y)

def subtract(a,b):
    c=a-b

r=subtract(3,2)
print(r)

def myfunc():
    print("welcome")

print(myfunc)
myfunc()
x=myfunc
x()

print("----------------Local/Global variables----------")
a=1000

def f1():
    b=2000
    global a #farward declaration
    a=5000
    print(b)
    print(a)
def f2():
    c=3000
    print(a)
    print(c)
f1()
print("----------")
f2()

def f1():
    print("i am in f1")
    f1()

# f1()

i=0
def f2():
    global i
    print("i am in f2",i)
    i=i+1
    while i<=5:
        f2()

f2()

print("===========lambda functions===============")

#normal function to calculate square

def square(x):
    return x*x

print(square(10))

myfunc = lambda x : x*x
a=myfunc(10)
print(a)

def cube(a,sqare):
    return a*sqare(a)

x=cube(10,lambda b:b*b)
print(x)

my_list = [1,5,4,6,8,11,13,12]

new_list = list(filter(lambda x:x%2==0, my_list))
print(new_list)

my_list = ['1','5','4','6','8','11','13','12']
new_list = list(map(lambda x:int(x)*int(x), my_list))
print(new_list)

# import functools
from functools import reduce

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(reduce(lambda a, b: a+b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(reduce(lambda a, b: a if a > b else b, lis))

print('max',max(lis))


def corefunc():
    print("it is from functions.py")
