t=()
print(t)
print(type(t))
a=tuple()
print(a)
print(type(a))
b=1,2,3
print(b)
print(type(b))
c=1,
print(c)
print(type(c))

p=(10,20,30,40,50,10,20,10,2.3,[1,2],(1,2),'yogi')
print(p)
print(p[-1])
print(p[0])
#p[1]=100 TypeError: 'tuple' object does not support item assignment
print(p.count(10))
print(p.index(20))
print("========nested tuple===========")
x = ((10,20,30),(40,50,60),(70,80,90))
print(len(x))
for i in x:
    print(i)
    for j in i:
        print(j)

print("========list in tuple===========")

x = ((10,20,30),[40,50,60],(70,80,90))
print(x)
print(x[1][1])
x[1][1]=100
print(x[1][1])
x[0][1]=100