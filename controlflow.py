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