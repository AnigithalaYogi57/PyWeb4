# print('yogi')) #syntax error
'''
try:
    i=int(input("enter a positive number:"))
    print(i)
except KeyError:
    print("key missing")
except ValueError:
    print("Invalid input, please enter numeric only.")

print('begin')
try:
    i = int(input("Enter fno."))
    j = int(input("Enter sno."))
    k=i/j
    print(k)
except ValueError:
    print("enter numeric only")
except ZeroDivisionError:
    print("whoops! can't divide by 0")
except:
    print("error occurred")
finally:
    print("Thank you visit again.")

print("end")
'''
try:
    x=int(input("enter a fnumber:"))
    y=int(input("enter a snumber:"))
    try:
        z=x/y
        p=int(input("enter a number:"))
    except ValueError:
        print("inner try value error handled")
except KeyError:
    print("it is handled by outer try except")
except ZeroDivisionError:
    print("outer try except zero division handled")