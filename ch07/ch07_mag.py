# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:14:36 2018

@author: nahas
"""

userInput = input("please give a number ")
#TypeError: unsupported operand type(s) for -: 'str' and 'int cause userInput is not
#a int type but a str type
print(type(userInput))

userInput(input("Please give a number "))

def simpleOperation(userInput):
    result = userInput - 2
    return result

def nestedOperation(result):
    result = simpleOperation(userInput)
    result2 = result * 2
    return result2

result = simpleOperation(userInput)
result2 = nestedOperation()

print(result2)
