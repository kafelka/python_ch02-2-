# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:09:06 2018

@author: mag
"""
#ex1 repeated division
x = 33
while x >= 1:
    print(x, ": ", end=' ')
    x = x / 2  
print(x)

#n + (n-1) +...+ 2 + 1

#ex2 triangular numbers
def triangular(n):
    numx3 = 0
    while n > 0:
        numx3 = numx3 + n
        n = n - 1
    return numx3

print(triangular(1))   
print(triangular(2))
print(triangular(3))
print(triangular(4))
print(triangular(5))
print(triangular(6))

#ex3 student marks
mark = 1
while mark > 0:
    mark = int(input("What's your mark: "))
    print("Your mark is", mark, end = ". ")
    if mark >= 70:
        print("First class!")
    elif mark >= 40:
        print("Pass!")
    else:
        print("Oh no, that's a fail...")  

print("***********************") 
i = 55
while i > 10:
    print(i)
    i = i * 0.8
    if i == 35.2:
        break


#ex4 break statement in a while loop
while True:
    name = input("What's your name? ")
    if name == "done":
        break
    print("Hello", name)
    
#ex5 guessing game - in a separate file
#ex6 dice game - in a separate file       
    