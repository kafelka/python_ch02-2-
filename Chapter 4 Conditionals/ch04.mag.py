# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 11:47:35 2018

@author: maggie
"""
import random
import datetime
import time

#if, elif, else - using conditional statements

number = input("Enter a number between 1 and 10: ")
number = int(number) 

if number > 10:
    print("Too high!")
elif number <= 0:
    print("Too low!")
else:
    print("Correct.")
    
#########################################################
#if I change the order of elif statement, the result will be different
age = input("Enter your age: ")
age = int(age) 

if age < 13:
    print("child")
elif age < 18:
    print("teen")
elif age < 95:
    print("adult")
else:
    print("Most probably you're dead. RIP.")

###############################################
def checkTeen(age):
    if age >=13 and age <=19:
        print("You're a teen")
    else:
        print("You're not a teen.")
    
checkTeen(20)


def luckyNumberRandom():
    name = input("Please type your name here: ")
    print ("hello " + name.upper())
    number = int(input("Please give a number "))
    
    print("Your lucky number is: " + str(random.randint(1, number)))

#######################################################
    
startTime = time.time()
print("date and time: ", datetime.datetime.now())
print()
print("current time: ", datetime.datetime.now().time())

luckyNumberRandom()

processTime = time.time()-startTime

print()
print("Program running time:", round(processTime, 2),"second")

###############################################################

#testing for teenagers
age = 15
isaTeen = age >= 13 and age <= 19
print(isaTeen)

age = 22
isaTeen = age >= 13 and age <= 19

print(isaTeen)


    
    
    