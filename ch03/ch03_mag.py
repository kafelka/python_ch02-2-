# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:54:59 2018

@author: nahas
"""
#print("What is your name?")
#name = input()
#
##name = input("What's your name?")
##print("Hello {}!".format(name))
#
##name3 = input().upper()
#
#name2 = name.capitalize()
#print("Hello {}!".format(name2))
#
#city = input("What's your city?")
#print ("Hello {} from {}.".format(name2,city))

#def hello_world():
#    print("Hello world!")
#    addition()
#
#def addition():
#    add2_3 = 2+3
#    print(add2_3)
#    print(2+6)
#    
#hello_world()

#def hi_maggie():
#    name = input("What's your name?").capitalize()
#    print("Hello {}!".format(name))
##    print("Hello Maggie!")
#    random1 = input("Provide a random number.")
#    random2 = input("Provide another random number.")
#    print(int(random1) + int(random2))
#    
#hi_maggie()

#def hello_world_3args(a,b,c):
#    print ("{}{}{}".format(a,b,c))
#    
#a1 = "hello "
#b1 = "world "
#c1 = "it's "
#a2 = "love "
#b2 = "coding"
#c2 = "Monday "
#a3 = "I think I "
#c3 = "again!"
#hello_world_3args(a1,b1,c3)
#hello_world_3args(a3,a2,b2)
#hello_world_3args(c1,c2,c3)
#
#print(range(10))
#print(range(1,10))
#print(range(1,10,2))
#
#def add_two_numbers(a,b):
##     print (5 + 3)
#     print (a + b)
#     
#a1 = 6
#b1 = 7
#     
##add_two_numbers()
#add_two_numbers(a1,b1)

def tempConverter(celsius):
    
    fahrenheit = celsius * 9.0 /5.0 + 32
    kelvin = celsius + 273.15
    
    print("That's {} degrees in fahrenheit and {} degrees in kelvin.".format(fahrenheit, kelvin))
    
celsius = int(input("What's the temperature in your city today?"))
    

tempConverter(celsius)
