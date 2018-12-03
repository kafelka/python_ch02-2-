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

def hello_world_3args(a,b,c):
    print ("{}{}{}".format(a,b,c))
    


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
    


#####the below does not work!!!!!!!!!!
#celsius = int(input("What's the temperature in your city today?"))
#
#def tempConverter2(celsius):
#    
#    fahrenheit = celsius * 9.0 /5.0 + 32
#    kelvin = celsius + 273.15
#    
#    return "That's {} degrees in fahrenheit and {} degrees in kelvin.".format(fahrenheit, kelvin)
#    
#tempConverter2(celsius)



#def tempConv(celsius):
#    fahrenheit = celsius * 9.0 /5.0 + 32
#    kelvin = celsius + 273.15
#    return (fahrenheit, kelvin)
#
#celsius = 10
#
#fahrenheit, kelvin = tempConv(celsius)
#print(fahrenheit, kelvin)


#def convTemp():
#    celsius = int(input("What's the temperature in your city today?"))
#    fahrenheit = celsius * 9.0 /5.0 + 32
#    kelvin = celsius + 273.15
#    print("Converting temp in c to fahrenheit and kelvin...")
#    print("That's {} degrees in fahrenheit and {} degrees in kelvin.".format(fahrenheit, kelvin))
#    return (fahrenheit, kelvin)
#
##convTemp()
#kelvin, fahrenheit = convTemp()


#def convert_temp_kelvin(celsius):
#    kelvin = celsius + 273.15
#    
#    return kelvin
#
#def convert_temp_fahr(celsius):
#    fahr = (celsius + 9.0) / 5.0 = 32
#    
#    return fahr
#
#def convert_temp_kelvin_to_fahr(celsius):
#    kelvin1 = convert_temp_kelvin(celsius)
#    fahr = ((kelvin1 * 9) /5) - 459.67
#            
#    print("Converting temp in kelvin to fahr.")
#    print("Temp in kelvin:", kelvin1)
#    print("Temp in fahr:", fahr)
#    
#    mainResult = kelvin1
#    return mainResult
#
#mainResult = convert_temp_kelvin_to_fahr(celsius2)


def convertDistance(miles):
    kilometers = (miles * 1.609)
    print("Converting distance in miles to kilometers.")
    print("Distance in miles:", miles)
    print("Distance in kilometers:", kilometers)
    
    return ("miles:" + str(miles), "kilometeres" + str(kilometers))




#def convertDistance():
#    miles = int(input("How many miles did you run last weekend?"))
#    kilometers = (miles * 1.61)
#    print("The distance you run is {} in miles and {} in kilometers.".format(miles, kilometers))
#    
#    return (miles, kilometers)
#
#convertDistance()
#
#def convertDistance(miles):
#    kilometers = (miles * 1.61)
##    print("The distance you run is {} in miles and {} in kilometers.".format(miles, kilometers))
#    return ("The distance in miles is: " + str(miles) + " and the distance in kilometers is: " + str(kilometers))
#
#convertDistance(1)
#
#London_Bristol = convertDistance(118)
#print(London_Bristol)
#London_Cardiff = convertDistance(150.6)
#London_Brighton = convertDistance(67)
#London_Birmingham = convertDistance(126)

##importing

#import math
##print(pi)
#print(math.pi)

##*******different way of importing
#from math import *
#print(pi)
#
#from math import pi


#import ch03_filename