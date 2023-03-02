
def make_pretty(fun):
    def inner():
        print("i got decorated")
        fun()
    return inner


@make_pretty
def oridnary():
    print("i am ordinary")

oridnary()

print("---------------")

def smart_divide(func):
    def inner(a,b):
        print("i am going to divide")
        if b==0:
            print("can't divide")
            return None
        func(a,b)
    return inner

@smart_divide
def divide(a,b):
    print(a/b)

divide(10,2)