# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:37:03 2018

@author: nahas
"""
name = input("What's your name? ")
print("Hello {}!".format(name.title()))

response = input("Do you live in London? y/n ")

if response == "n":
    print("Oh... You should visit it!")
elif response == "y":
    print("you answered yes")
#     activity_selection = input("Imagine you have a day for yourself in London. What sort of activity would you be interested in? Type e for entertainment, f for food, c for cultural or s for shopping")
#     if activity_selection = "e":
#         
         
else: 
    print("Wrong answer. Go back to your city :P")
    
    
class Activity():
    def __init__(self, budget=0, ):
        self.budget = budget
        
        
        
class Entertainment(Activity):
    def __init__(self, budget=0):
        
        
