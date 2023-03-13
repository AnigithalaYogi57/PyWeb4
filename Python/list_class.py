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

'''
'''
x=[10,20,30,40,50,60]

i=0
s=0
while i<len(x):
    s=s+x[i]
    i=i+1
print('sum=',s)

a='Yogi A'
l=a.split()
print(l)
l=list(a)
print(l)

r=""
for chr in l:
    r=r+chr
print(r)


print("#".join(l))

x = [[10,20,30],[40,50,60],[70,80,90]]
a,b,c=x
print(a)
print(b)
print(c)
'''
print("============methods of list class===================")
x=[10,20,30,40,50,60,10]
print(x)
x.append(100)
print(x)
print(x.count(10))
print(x.index(10))
y=x.copy()
print(y)
x.insert(2,123)
print(x)
x.remove(123)
x.remove(10)
print(x)
x.pop()
x.pop(2)
print(x)
z=[80,70,90]
x.extend(z)
#x.append(z)
print(x)
# x.sort(reverse=True)
# print(x)
x.reverse()
print(x)
x.clear()
print(x)

print("=============remove the duplicates====================")

x=[1,2,1,3,4,2,4,5,7,8,9,64,457,98,2,3,56,79,9,1,2,4,8,9,10]

nl = []
for elm in x:
    if elm not in nl:
        nl.append(elm)
print(nl)

print("================List comprehension===========")
x = [p for p in range(1,11)]
print(x)

nl=[]
for i in range(1,11):
    nl.append(i)
print(nl)

nl=[]
for i in range(10,22):
    if i%2==0:
        nl.append(i**2)
print(nl)

y=[p*p for p in range(10,22) if p%2==0 ]
print(y)