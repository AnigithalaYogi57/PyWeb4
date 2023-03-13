'''
def my_gen():
    n=1
    print("This is printed first")
    yield n
    n+=1
    print("This is printed second")
    yield n
    n+=1
    print("This is printed at last")
    yield n

it1=my_gen()
print(next(it1))
print(next(it1))
print(next(it1))
'''
'''
l=(p*p for p in range(1,11))
print(l)
for e in l:
    print(e)
'''

def rev_str(my_str):
    l = len(my_str)
    for i in range(l-1,-1,-1):
        yield my_str[i]

it=rev_str("python")
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break

for i in it:
    print(i)

print("=================closures=======================")

def outer():
    print("i am in outer func")
    def inner():
        print("i am in inner func")
    # inner()
    return inner

res = outer()
del outer
res()
# outer() #NameError
