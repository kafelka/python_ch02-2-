# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 09:28:59 2019

@author: mag
"""
#Ex1 initialise person class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        if gender  == "m":
            self.isMale = True
        elif gender == "f":
            self.isMale = False
        else:
            print("Gender not recognised!")


    def greetingInformal(self):
        print("Hi", self.name)
    
    def greetingFormal(self):
        if self.isMale:
            print("Welcome Mr", self.name)
        else:
            print("Welcome Ms", self.name)
            
#     ex3 greeting filter       
    def greetingAgeBased(self):
        if self.age < 18:
            print("Welcome, young", self.name)
        elif self.age > 60:
            print("Welcome, venerable", self.name)
        else:
            self.greetingFormal()
            
#4 Create a subclass for the Person class
class Wizard(Person):
    def __init__(self, name, age, gender):
#  ex5       Redefine init
        Person.__init__(self, name, age, "m")
        self.name = name
        self.age = age
        self.isMale = True
        
    def greetingFormal(self):
        print("Welcome, Mr", self.name, end=" ")
        print("- you\'re a fine wizard!")
  
#ex6 New method for Wizard      
    def spell(self):
        print("Expelliarmus!")
        

            
#ex2 More functionalities
p1 = Person("Clare", 62, "f")
p2 = Person("Max", 28, "m")
p3 = Person("Barry", 65, "m")
p4 = Wizard("Harry", 12, "m")

p1.greetingFormal()
p2.greetingInformal()
p1.greetingAgeBased()
p2.greetingAgeBased()
p3.greetingAgeBased()
p4.greetingFormal()
p4.spell()





