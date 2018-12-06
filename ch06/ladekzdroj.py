# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 18:31:14 2018

@author: nahas
"""
def ask_london():
    response = input("Do you live in London? y/n ")
    if response.lower() == "y":
        print("Nice!")
        return True
    elif response.lower() == "n":
        print("Oh, maybe you should come and visit it?")
        return False
    else:
        print("Please answer by typing y or n.")
        return ask_london()
    
    
def ask_activity():
    activity = input("""
 What sort of activity would you be interested in?
 Type first letter:
    * e for entertainment
    * s for shopping
    * c for cultural
    * f for food """)
        
        
    if activity.lower() == "e" or activity.lower() == "s" or activity.lower() == "c" or activity.lower() == "f":
    #if activity.lower() in ["e", "s", "c", "f"]
        print(f"Good choice! You selected: {activity}.")
        return activity.lower()
    else:
        print("Type first letter of the activity.")
        return ask_activity()
        
    
def ask_budget():
    
    budget = int(input("What's your budget in $? ")) #change to GBP
#    # try - tries to do an action that can fail, remove int above first!
#    try: 
#        budget = int(budget)
#    except: #action failed, do the following:
#        print("Type a positive number.")
#        return ask_budget()
    
    if budget >= 0:
        return budget
    else:
        print("Type a positive number.")
        return ask_budget()
    
    
class Activity():
    def __init__(self, budget=0):
        self.budget = budget
        
        
class Entertainment(Activity):
    def __init__(self, budget=0):
        if budget <= 25:
            print("Your options are: A, B or C")
        elif (budget > 25 and budget < 75):
            print("Your options are: D, E or F")
        else:
            print("Your options are: G, H or I")
            
    def entertainment_costam(self):
        print("Blablabla")
            
class Food(Activity):
     def __init__(self, budget=0):
        if budget <= 25:
            print("Your options are: J, K or L")
        elif (budget > 25 and budget < 75):
            print("Your options are: M, N or O")
        else:
            print("Your options are: P, R or S")
            
class Cultural(Activity):
    def __init__(self, budget=0):
        if budget <= 25:
            print("Your options are: T, U or V")
        elif (budget > 25 and budget < 75):
            print("Your options are: X, Y or Z")
        else:
            print("Your options are: AA, BB or CC")
            
class Shopping(Activity):
    def __init__(self, budget=0):
        if budget <= 25:
            print("Your options are: T, U or V")
        elif (budget > 25 and budget < 75):
            print("Your options are: X, Y or Z")
        else:
            print("Your options are: AA, BB or CC")


    
name = input("What's your name? ")
print("Hello {}!".format(name.title()))

#if ask_london is false, stop the program.
#if not ask_london():
    #stop the program - google it

is_london = ask_london()
activity_type = ask_activity()
user_budget = ask_budget()


if activity_type == "e":
    x = Entertainment(user_budget)
    x.entertainment_costam()
if activity_type == "s":
    Entertainment(user_budget)
if activity_type == "c":
    Entertainment(user_budget)
if activity_type == "f":
    Entertainment(user_budget)
    
    
   

#--------------------------------