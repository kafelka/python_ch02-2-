# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:09:06 2018

@author: mag
"""
x = 33
while x >= 1:
    print(x, ": ", end=' ')
    x = x / 2  
print(x)

#n + (n-1) +...+ 2 + 1

def someMaths(n):
    numx3 = 0
    while n > 0:
        numx3 = numx3 + n
        n = n - 1
    return numx3

print(someMaths(1))   
print(someMaths(2))
print(someMaths(3))
print(someMaths(4))
print(someMaths(5))
print(someMaths(6))