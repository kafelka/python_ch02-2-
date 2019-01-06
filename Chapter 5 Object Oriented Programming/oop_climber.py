#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 16:58:10 2019

@author: kafelka
"""

#UNFINISHED class Human
class Human():
    def __init__(self, name, stamina=0):
        self.name = name.title()
        self.stamina = stamina
        
    def greeting(self):
        print(f"Hello {self.name}!")
        
    def isClimber(self):
        return input("Have you ever been climbing? Y/N ").lower()
            
    
class Climber(Human):            
    def __init__(self, name, experience=0, stamina = None):
        Human.__init__(self, name)
        self.experience = experience
        if stamina == None:
            self.calcStamina()
        else:
            self.stamina = stamina
            
    def greeting(self):
        print(f"Bye climber {self.name}!")
        
        
    def calcStamina(self):
        if self.experience < 1:
            self.stamina = 1
            print("I bet you have a lot of fun. Keep doing it!")
        elif 1 <= self.experience < 2:
            self.stamina = 2
            print("You have less than " + self.stamina + " years of climbing experience. I bet you like challenges!")
        elif  2 <= self.experience < 4:
            self.stamina = 3
            print("You are quite a strong climber, have you tried v6s yet? ;-)")
        else:
            self.stamina = 4
            print(f"You have over {self.experience} years of climbing experience. All you need is some chalk and coffee.")


class ModerateCoffeeDrinker(Climber):
    def __init__(self, name, experience, espresso, stamina):
        Climber.__init__(self, name, experience, stamina)
        self.espresso = espresso
        
    def completedRoutes(self):
        self.routes = self.espresso * self.stamina
        print(f"You will be able to complete around {self.routes} routes today. Are you sure you do need more coffee? ;-)")
        
    
class CoffeeAddict(Climber):
    def __init__(self, name, experience, espresso, stamina):
        Climber.__init__(self, name, experience, stamina)
        self.espresso = espresso
    
    def completedRoutes(self):
        self.routes = self.espresso * self.stamina * 3
        print(f"You're going to smash it! At least {self.routes} routes today!")
    
    
class NonClimber(Human):
    def __init__(self, name, motivation):
        Human.__init__(self, name)

        self.motivation = motivation
        
    def motivationLevel(self):
        if motivation == 0:
            print("Oh, ok, maybe you should try something else instead.")
        elif motivation == 1 or motivation == 2:
            print("Nice, schedule your induction classes at your local climbing gym, I'm sure you're going yo enjoy it!")
        elif motivation >= 3:
            print("That's the spirit! Find your local climbing gym and give it a go! You're going to love it!")
        
        
name = input("What's your name? ")
person = Human(name)
person.greeting()
isClimber = person.isClimber()
if isClimber == "y":
    experience = int(input("How long have you been climbing (years)? "))
    person = Climber(name, experience)
    espresso = int(input("How many coffees did you drink before climbing session? "))
    if 1 <= espresso < 3:
        person = ModerateCoffeeDrinker(name, experience, espresso, person.stamina)
        person.completedRoutes()
    else:
        person = CoffeeAddict(name, experience, espresso, person.stamina)
        person.completedRoutes()
    person.greeting()
else:
    motivation = int(input("How about trying it? What's your motivation on a scale from 0 to 3? "))
    person = NonClimber(name, motivation)
    person.motivationLevel()