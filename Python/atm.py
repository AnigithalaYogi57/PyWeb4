print("Welcome to State Bank Of India")
p=int(input("Enter your 4 digit PIN:"))
#my pin is 1234
#my accoutn balance is 25000
m=25000
if p == 1234:
    print("1-withdraw")
    print("2-BalanceEnquiry")
    print("3-FastCash")
    c = int(input("please choose the option:"))
    if c==1:
        w = int(input("Enter withdraw amount:"))
        if w<=m and w%100 == 0:
            m=m-w
            print("Please take your cash:",w)
            print("Thank you.")
        else:
            print("invalid cash")

    elif c==2:
        print("Your available balance is:",m)
    elif c==3:
        print("1-->5,000")
        print("2-->10,000")
        print("3-->15,000")
        print("4-->20,000")
        f = int(input("Enter fast cash option:"))
        if f==1 and 5000<=m:
            print("Please take your cash 5000")
        elif f==2 and 10000<=m:
            print("Please take your cash 10000")
        elif f==3 and 15000<=m:
            print("Please take your cash 15000")
        elif f==4 and 20000<=m:
            print("Please take your cash 20000")
        else:
            print("invalid fast cash option.")
    else:
        print("invalid choice.")
else:
    print("wrong pin")