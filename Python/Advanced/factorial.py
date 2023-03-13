import sys

def factoral(n):
    if n==0:
        return 1
    return n*factoral(n-1)


def division(n):
    d = 10/n
    return d


if __name__ == "__main__":
    print("in factorial file",__name__)
    try:
        n = int(sys.argv[1])
        f = factoral(n)
        print(f)
        res=division(n)
        print(res)
    except IndexError:
        print("pass one command line argument")
    except ZeroDivisionError:
        print("Can't divide by 0")
    except Exception:
        print("error occured")
