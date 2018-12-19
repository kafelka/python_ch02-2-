# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:54:59 2018

@author: maggie
"""
#input from user

print("What is your name?")
name = input()

name = input("What's your name? ")
print("Hello {}!".format(name))


name2 = name.capitalize()
print("Hello {}!".format(name2))

city = input("What's your city? ")
print ("Hello {} from {}.".format(name2,city))

#ex2 first function

def hello_world():
    print("Hello world!")
    addition()

def addition():
    add2_3 = 2+3
    return add2_3

print(addition())
hello_world()

def hi_maggie():
    name = input("What's your name? ").capitalize()
    print("Hello {}!".format(name))
#    print("Hello Maggie!")
    random1 = input("Provide a random number: ")
    random2 = input("Provide another random number: ")
    print(int(random1) + int(random2))
    
hi_maggie()

#######################################
def hello_world_3args(a,b,c):
    print ("{}{}{}".format(a,b,c))

#moved to test file: 
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

#ex3   
print(range(10))
print(range(1,10))
print(range(1,10,2))

#ex4 adding two numbers
def add_two_numbers(a,b):
#     print (5 + 3)
     print (a + b)
     
a1 = 6
b1 = 7
     
#add_two_numbers()
add_two_numbers(a1,b1)

#with return

def add_two_numbers2(a,b):
#     print (5 + 3)
    return a + b
     
a1 = 4
b1 = 21
     
#add_two_numbers()
print(add_two_numbers2(a1,b1))

    
#temperature conversion exercise

def tempConverter(celsius):
    
    fahrenheit = celsius * 9.0 /5.0 + 32
    kelvin = celsius + 273.15
    
    print("That's {} degrees in fahrenheit and {} degrees in kelvin.".format(fahrenheit, kelvin))
    
userInput = int(input("What's the temperature in your city today?"))
    
tempConverter(userInput)


#ex 5 version with return
userInput = int(input("What's the temperature in your city today?"))

def tempConverter2(celsius):
    
    fahrenheit = celsius * 9.0 /5.0 + 32
    kelvin = celsius + 273.15
    
    return "That's {} degrees in fahrenheit and {} degrees in kelvin.".format(fahrenheit, kelvin)
    
print(tempConverter2(userInput))
result = tempConverter2(userInput)
print(result)

#another version

def tempConv(celsius):
    fahrenheit = celsius * 9.0 /5.0 + 32
    kelvin = celsius + 273.15
    return (fahrenheit, kelvin)

userInput = 10

outputFahr, outputKel = tempConv(userInput)
print(outputFahr, outputKel)

#another version
def convTemp():
    celsius = int(input("What's the temperature in your city today?"))
    fahrenheit = celsius * 9.0 /5.0 + 32
    kelvin = celsius + 273.15
    print("Converting temp in c to fahrenheit and kelvin...")
    print("That's {} degrees in fahrenheit and {} degrees in kelvin.".format(fahrenheit, kelvin))
    return (fahrenheit, kelvin)

#convTemp()
kelvin, fahrenheit = convTemp()

#another version
    
def convert_temp_kelvin(celsius):
    kelvin = celsius + 273.15
    
    return kelvin

def convert_temp_fahr(celsius):
    fahr = (celsius * 9.0) / 5.0 + 32
    
    return fahr

def convert_kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    
    return fahrenheit


def convert_temp_kelvin_to_fahr(celsius):
    kelvin = convert_temp_kelvin(celsius)
#    fahr = convert_temp_fahr(celsius)
    fahr = convert_kelvin_to_fahrenheit(kelvin)
            
    print("Converting temp in kelvin to fahrenheit.")
    print("Temp in kelvin:", kelvin)
    print("Temp in fahrenheit:", fahr)
    
    mainResult = kelvin
    return mainResult

userInput = int(input("What's the temperature in your city today?"))
mainResult = convert_temp_kelvin_to_fahr(userInput)
#
#########################################
#
def convertDistance(miles):
    kilometers = int(miles * 1.609)
    print("Converting distance in miles to kilometers.")
    print("Distance in miles:", miles)
    print("Distance in kilometers:", kilometers)
    
    return ("miles:" + str(miles), "kilometeres" + str(kilometers))

convertDistance(10)
#
#########################################
    
def convertDistance():
    miles = int(input("How many miles did you run last weekend?"))
    kilometers = (miles * 1.61)
    print("The distance you run is {} in miles and {} in kilometers.".format(miles, kilometers))
    
    return (miles, kilometers)

convertDistance()

#miles - km game
#
def convertDistance(miles):
    kilometers = (miles * 1.61)
    return ("The distance you run is {:.1f} in miles and {:.1f} in kilometers.".format(miles, kilometers))
#    return ("The distance in miles is: " + str(miles) + " and the distance in kilometers is: " + str(kilometers))


London_Bristol = convertDistance(118)
print(London_Bristol)
London_Cardiff = convertDistance(150.6)
London_Brighton = convertDistance(67)
London_Birmingham = convertDistance(126)

###importing
#
##import math
###print(pi)
##print(math.pi)

##*******different way of importing
#from math import *
#print(pi)
#
#from math import pi


#import ch03_filename