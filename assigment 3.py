'''
TASK 1
'''
import math

n=int(input("ENTER YOUR NUMBER :-  "))

def add(n):

    if n<2:
        return 1

    else:
        return n* add(n-1)

a= add(n)
print('FACTORAL OF' , n, 'is', a)

'''
TASK 2
'''

num=int(input("ENTER THE VALUE :-  "))

from math  import *

print('Square root of',num,'is',math.sqrt(num))

print('log of ',num,'is',math.log(num))

print('sin of ',num,'is',math.sin(num))
