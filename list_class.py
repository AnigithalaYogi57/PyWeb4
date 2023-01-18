'''
a=[]
print(type(a))
b=list()
print(len(a))
print(len(b))
print(type(b))
x=[1,2,3,4,10.5,'yogi',True,2,2,'yogi',2,3]
print(x)
print(len(x))
x=[10,20,30,40,50,60]
print(x)
print(x[1])
print(x[1:5])
print(x[1:])
print(x[-1])
'''
x=[10,20,30,40,50,60]
print(x)
s=0
for i in x:
    s+=i
    #s=s+i
print(s)
print('total=',sum(x))
x[1]=100
print(x)
print(x[1])
print('length=',len(x))
print(x[len(x)-1])
#print(x[len(x)]) IndexError

x = [[10,20,30],[40,50,60],[70,80,90]]
print(len(x))
print(x[0])
print(x[2][0])

for j in x:
    print(j, type(j))
    for k in j:
        print(k,type(k))

y=[10,20,30,40,50,60,70,80]
for d in y:
    print(d)
print("--------------------")
for e in range(10,90,10):
    print(e)

A=[10,20,30,40,50,60,70,80]

se = int(input("Enter search element:"))

if se in A:
    print('element is found')
else:
    print('element is not found')