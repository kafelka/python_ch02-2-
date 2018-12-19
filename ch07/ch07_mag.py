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

#set up a breakpoint in order to run the code in debugging mode
#the red dot next to the line of code (double click)
#spyder toolbar:
#    first button is to start running the code until breakpoint
#    second button allows running code line by line till breakpoint
#    third button is for stepping into sections(classes, functions) that you would
#    like to explore 
#    fourth button is to step out of the third button
#    fourth button - go to the next breakpoint
#    square shaped button - exit debugging mode