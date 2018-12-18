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

#mark = 1
#while mark > 0:
#    mark = int(input("What's your mark: "))
#    print("Your mark is", mark, end = ". ")
#    if mark >= 70:
#        print("First class!")
#    elif mark >= 40:
#        print("Pass!")
#    else:
#        print("Oh no, that's a fail...")
   
#didYouPass = 'Yes'
#
#while didYouPass == 'Yes':
#
#   mark = int(input('What is your score? '))
#   
#   if mark >= 70 and mark <=90:
#       print('FIRST CLASS')
#
#   elif mark >= 40:
#       print('PASS')
#
#   elif mark < 40:
#       print('FAIL')
#
#   didYouPass = input('Did you pass? ')

print("***********************") 
i = 55
while i > 10:
    print(i)
    i = i * 0.8
    if i == 35.2:
        break

print("***********************") 
while True:
    name = input("What's your name? ")
    if name == "done":
        break
    print("Hello", name)
    
        
    