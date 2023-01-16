'''
print("===========conditionala statements==========")
print('begin')
x=input("Enter positive number:")
i = int(x)
if i<10:
    print("given number is 1 digit number")
elif i<100:
    print("given number is 2 digit number")
elif i<1000:
    print("given number is 3 digit number")
elif i<10000:
    print("given number is 4 digit number")
else:
    print("given number is >4 digit number")
print('end')
'''
'''
print("===========looping statements==========")
print('begin')
i=1
while i<=5:
    print('welcome')
    i=i+1
    #i+=1
print("end")

print('begin')
i=1
s=0
while i<=100:
    s=s+i
    i=i+1
else:
    print("while condition became false, i.e calculation is done!")

print('sum=',s)
print('end')

i=0
while True:
    i=i+1
    print(i)
    if i==10:
        break

i=0
while i<5:
    i=i+1
    if i==3:
        continue
    print("welcome",i)

#uname=AYogi
#pwd = Test@123
while True:
    name = input("Enter username:")
    if name != 'AYogi':
        continue
    password = input("Hello, AYogi, what is the password:")
    if password == 'Test@123':
        break
print("Access granted")

for i in 'yogi':
    #print('welcome')
    print(i)
'''
for i in range(1,10,2):
    print(i)