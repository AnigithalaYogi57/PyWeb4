# import pack1.mod1

# print(pack1.mod1.msg)

import pack1.mod1 as m1

print(m1.a)
print(m1.msg)

from pack1.subpack1 import mod2
# from pack1.subpack1.mod2 import b,msg1
# print(b,msg1)

print(mod2.b)
print(mod2.msg1)