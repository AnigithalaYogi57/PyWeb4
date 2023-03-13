class TwoPow:
    def __init__(self,m=0):
        self.m = m

    def __iter__(self):
        self.n=0
        return self

    def __next__(self):
        if self.n<=self.m:
            r = 2**self.n
            self.n+=1
            return r
        else:
            raise StopIteration

p1=TwoPow(5)
it1=iter(p1)
'''
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
# print(next(it1))
'''
'''
while True:
    try:
        print(next(it1))
    except StopIteration:
        break
'''
for i in it1:
    print(i)

l=[10,20,30,40]
# for i in l:
#     print(i)

it1=iter(l)
try:
    print(next(it1))
    print(next(it1))
    print(next(it1))
    print(next(it1))
    print(next(it1))
    print(next(it1))
    print(next(it1))
    print(next(it1))
except StopIteration:
    pass
