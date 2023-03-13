class customer:
    """This is a customer class"""
    cbname = "sbi"
    obj_counter = 0
    def __init__(self, name, add, acno, bal):
        customer.obj_counter += 1
        self.cname = name
        self.cadd = add
        self.cacno = acno
        self.cbal = bal
    def display(self):
        print("Bank Name:",customer.cbname)
        print("Customer Name:",self.cname)
        print("Customer Account:",self.cacno)

    def deposit(self, damt):
        self.cbal += damt

    def withdraw(self, wamt):
        self.cbal -= wamt

    def bal_enq(self):
        print("Hello {}, Your current balance is:".format(self.cname), self.cbal)


c1=customer("Yogi","hyd",62087118670, 50000)
c2=customer("Naveen","Bang",62087118671, 60000)
c3=customer("Naresh","chennai",62087118691, 70000)
c4=customer("ravi","chennai",62087118791, 80000)
print("no. of objects created:", customer.obj_counter)
c2.display()
customer.display(c4)
c2.deposit(10000)
c2.bal_enq()
c3.bal_enq()
c1.bal_enq()
c2.withdraw(5000)
c2.bal_enq()
