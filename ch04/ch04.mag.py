# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 11:47:35 2018

@author: nahas
"""
import random
import datetime
import time

def luckyNumberRandom():
    name = input("Please type your name here: ")
    print ("hello " + name.upper())
    number = int(input("Please give a number "))
    
    print("Your lucky number is: " + str(random.randint(1, number)))
    
startTime = time.time()
print("date and time", datetime.datetime.now())
print()
print("current time", datetime.datetime.now().time())

luckyNumberRandom()

processTime = time.time()-startTime

print()
print("Program running time:", round(processTime, 2),"second")

################################################################

