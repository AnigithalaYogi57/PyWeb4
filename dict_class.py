d={}
print(d)
print(type(d))
e=dict()
print(e)
print(type(e))

f={'python':99,'java':90,'oracle':82,'django':97}
print(f)
print(type(f))
print(len(f))

g = {}
g['a']=10
g['b']=20
g['c']=30
print(g)

h=dict(a=10,b=20,c=50)
print(h)

i = {}
i.update({'first_name':'yogi','last_name':'A','age':30})
print(i)
i.update({'last_name':'B'})
print(i)
i.update({'id':1})
print(i)

j={1:1,2:4,1.5:'yogi',True:"yogi",(1,2,(4,5)):[3,4],1:10}
print(j)
k={'a':10,'a':20}
print(k)

x={'python':99,'java':90,'oracle':82,'django':97}
print(x)
print(x['python'])
print(x.get('java'))
print(x.get('php'))
#print(x['php'])
x.pop('oracle')
print(x)
x.popitem()
print(x)

y={'python':99,'java':90,'oracle':82,'django':97}
k=y.keys()
print(k)
v=y.values()
print(v)
itms = y.items()
print(itms)

# for itm in itms:
#     print(itm[0],itm[1])

for k,v in itms:
    print(k,v)

x = {p:p*p for p in range(5)}
print(x)
y={p:p*p for p in range(5,15) if p%2!=0}
print(y)