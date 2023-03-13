'''
import mod1

print(mod1.a)
print(mod1.b)

mod1.testmod()
'''

from mod1 import a, testmod
print(a)
testmod()

import keyword as kw
print(kw.kwlist)

from functions import corefunc as p
from mod1 import corefunc as q

p()
q()

import math as m
print(m.pi)
x=m.sqrt(100)
print('sqrt',x)
