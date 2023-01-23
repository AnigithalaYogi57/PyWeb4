s={1,2}
print(s)
print(type(s))
b=set()
print(b)
print(type(b))

s={4,3,2,5,6,2,5,6}

print('not insertion order:',s)

#s={[1,3],1,3,4} #unhashable type error
#print(s)

x={10,20,30,40,50}
print(x)
print(30 in x)

for p in x:
    print(p)

# y={(1,2,3),(4,5,6),(7,[1,2],9)}
# print(y)

#y={{1,2,3},{4,5,6},{7,8,9}}
#print(y)

print("================methods of set=====================")
# x={10,20,30,40,50}
# x = {p for p in range(10,60,10)}
x = eval(input('Enter a set:'))
print(x)
x.add(60)
print(x)
y=x.copy()
print(y)
# x.remove(100) #it will throw KeyError if element is not found
x.discard(100) #it will not throw KeyError
print(x)
x.pop()
print(x)
x.clear()
print(x)
print("==============set operations==============")
A={1,2,3,4,5}
B={4,5,6,7,8}
print("A=",A)
print("B=",B)
print("A|B=",A|B)
print("B|A=",B|A)
print(A.union(B))
print(B.union(A))
print("A&B=",A&B)
print("B&A=",B&A)
print(A.intersection(B))
print(B.intersection(A))
print("A-B=",A-B)
print("B-A=",B-A)
print(A.difference(B))
print(B.difference(A))
print("A^B=",A^B)
print("B^A=",B^A)
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

print("==============set comprahension===============")
x={p for p in range(10)}
print(x)

y={q*q for q in range(10,20) if q%2==0}
print(y)