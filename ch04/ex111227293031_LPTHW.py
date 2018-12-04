# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 15:26:01 2018

@author: nahas
"""
##ex11

#print("How old are you?", end=" ")
#age = input()
#print("How tall are you?", end=" ")
#height = input()
#print("How much do you weigh?", end=" ")
#weight = input()
#
#print(f"So, you're {age} years old, {height} tall and {weight} heavy.")
#
#print("***********")

#ex12
#age = input("How old are you? ")
#height = input("How tall are you? ")
#weight = input("How much do you weigh? ")
#
#print(f"So, you're {age} years old, {height} tall and {weight} heavy.")

#print("***********")

#ex28
#
#print(True and True)
#print(False and True)
#print(1==1 and 2==1)
#print("test"=="test")
#print(1==1 or 2!=1)
#print(True or 1==1)
#print(False and 0!=0)
#print(True or 1==1)
#print("test"=="testing")
#print(1!=0 and 2==1)
#print("test"!="testing")
#print("test"==1)
#print(not(True and False))
#print(not(1==1 and 0!=1))
#print(not(10==1 or 1000==1000))
#print(not(1!=10 or 3==4))
#print(not("testing"=="testing" and "Zed"=="Cool Guy"))
#print(1==1 and (not("testing"==1 or 1==0)))
#print("chunky"=="bacon" and (not(3==4 or 3==3)))
#print(3==3 and (not("testing"=="testing" or "Python"=="Fun")))

#print("***********")

#ex29
people = 20
cats = 30
dogs = 15

if people < cats: 
    print("Too many cats! The world is doomed")
    
if people > cats:
    print("Not many cats! The world is saved!")
    
if people < dogs:
    print("The world is drooled on!")
    
if people > dogs:
    print("The world is dry!")
    
dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")
    
if people <= dogs:
    print("People are less than or equal to dogs.")
    
if people == dogs:
    print("People are dogs.")
    
print("***********")
#ex30

people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars")
elif cars < people:
    print("We should not take the cars.")
else: 
    print("We can't decide.")
    
if trucks > cars:
    print("That's too many trucks")
elif trucks < cars:
    print("Maybe we could take the trucks")
else:
    print("We still can't decide.")
    
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

print("***********")    
#ex31

print("""You enter a dark room with two doors.
      Do you go through door #1 or door #2?""")
      
door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheesecake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    
    bear = input("> ")
    
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away")
        
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    
    insanity = input("> ")
    
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else: 
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
        
else:
    print("You stumble around and fall on a knife and die. Good job!")
