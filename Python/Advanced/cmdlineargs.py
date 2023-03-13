print("command line arguments")

import sys

print(sys.argv)
try:
    print(sys.argv[1])
    print(sys.argv[2])
    print(type(sys.argv[1]))
    print(type(sys.argv[2]))
except IndexError:
    pass