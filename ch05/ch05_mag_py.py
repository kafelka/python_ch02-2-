# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:07:41 2018

@author: nahas
"""

class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the following properties:
    Attributes:
        name: A string represeting the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0, age=0):
        """Return a Customer object whose name is *name* and starting balance is *balance*."""
        self.name = name
        self.balance = balance
        self.age = age
        
    def withdraw(self, amount):
        """Return balance remaining after withdrawing *amount* dollars."""
        if amount > self.balance:
            raise RuntimeError("Amount greater than available balance.")
        self.balance -= amount
        return self.balance
        
    def deposit(self, amount):
        """Return the balance remaining after depositing *amount* dollars."""
        self.balance += amount
        return self.balance
    
    
jason = Customer("Jason Taylor", 1000.0, 25)
#print(jason.balance)
#print(jason.name)
#print(jason.age)

jason.withdraw(100.0)
#print("Checking balance after withdrawing cash:")
#print(jason.balance)
#jason.withdraw(1000.0)
jason.deposit(800.0)
#print("Checking balance after deposit cash:")
#print(jason.balance)

maggie = Customer("Maggie K.", 2000.0)
#print(maggie.balance)
#print(maggie.name)
#print(maggie.age)
maggie.withdraw(200.0)

#cos mi tu nie dziala:
#withdrawAmount = float(input("How much did you withdraw today?"))
#print(maggie.withdraw(withdrawAmount))

#name1 = "Clare B"
#balance1 = 3000.0

#print("Type:", type(jason))

#print(list(range(10)))
#
#print(list(range(1,10)))
#
#print(list(range(1,10,3)))


#class Animal():
#    def eat(self):
#        print("Yum yum yum!")
#        
#class Dog(Animal):
#    def bark(self):
#        print("Woof, woof!")
#        
#class Cat(Animal):
#    def meow(self):
#        print("Meooow!")
#    def paws(self):
#        print("I've got 4 paws.")
        
#Snoopy = Dog()
#Snoopy.bark()
#Snoopy.eat()
#
#Cosmo = Cat()
#Cosmo.meow()
#Cosmo.paws()
#Cosmo.eat()

class Robot():
    def jump(self):
        print("Jumping to warm up.")
        
class Climber(Robot):
    def climbUp(self):
        print("I'm climbing up the wall.")
        
class Overhang(Climber):
    def overhangUp(self):
        print("I'm climbing up an overhanging wall.")
        
class Climber2(Robot):
    def climbDown(self):
        print("I'm climbing down.")
        
class Helper(Robot):
    def help(self):
        print("I am carrying heavy stuff.")
        
Morty = Helper()
Morty.help()

Max = Overhang()
Max.overhangUp()

#Chen's example
class Animal():
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        
    def eat(self):
         print('yum')
         
class Dog(Animal):
    def __init__(self, name, age=0,barkNumber=0):
        self.barkNumber = barkNumber
        
    def bark(self):
        print('Woof! '*self.barkNumber)
        
        
class DogAgent(Dog):
    def detect(self):
        if self.barkNumber>=3:
            print('strenger coming!!!')
        
class Cat(Animal):
    def meow(self):
        print('Meow')
name = input('what is your pet\'s name:')        
age = int(input('what is your pet\'s age: '))
bark = int(input('how many times you heard it barked: '))

dog007 = DogAgent(name, age, bark) #always inheritant ancester's
dog007.bark()
dog007.eat()
dog007.detect()

#class Human():
#    def __init__(self, name, age=0, stamina=0):
#        self.name = name
#        self.age = age
#        self.stamina = stamina
#        
#        def greeting(self):
#            print(f"Hello {self.name}!")
#            
#class Climber(Human):            
#    def __init__(self, name, age=0, stamina=0, experience=0, routes=0):
#        Human.__init__(self, name, age=0, stamina=0, experiece=0, routes=0)
#        self.routes = routes
#        self.experience = experience
#        
#        def stamina(self):
##            if self.experience < 1:
##                self.stamina = 1
##                print("I bet you have a lot of fun. Keep doing it!")
#            if self.experience > 1 and self.experience < 2:
#                self.stamina = 2
#                print("You have less than " + self.stamina + " years of climbing experience. I bet you like challenges!")
#            elif self.experience > 2 and self.experience < 4:
#                self.stamina = 3
#                print("You are a quite strong climber, have you tried v6s yet? ;-)")
#            else:
#                self.stamina = 4
#                print(f"You have over {self.stamina} years of climbing experience. All you need is some chalk and coffee.")
#
##class ModerateCoffeeDrinker(Climber):
##    def __init__(self, name, age=0, stamina=0, experience=0, routes=0, espresso=1)
##        self.espresso = espresso
##        
##        def completedRoutes:
##            self.espresso * self.stamina
##        
##        
##    
##class CoffeeAddict(Climber):
##    def __init__(self, name, age=0, stamina=0, experience=0, routes=0, espresso=3)
##    self.espresso = espresso
##    
#    
#class NonClimber(Human):
#    def __init__(self, name, age=0, stamina=0, routes=0, motivation=0):
#        self.routes = routes
#        self.motivation = motivation
#        
#        
#name = input("What's your name? ")
#print("Hello {}!".format(name)).title()    


class SuperRobot():
    def __init__(self):
        self.o1 = Robot()
        self.o2 = Dog()
        self.o3 = Cat()

    def playGame(self):
        print("alphago game")
    def move(self):
        return self.o1.move()
    def bark(self):
        return self.o2.bark()
    def clean(self):
        return self.o3.clean()
    
machineDog = SuperRobot()
machineDog.move()
machineDog.bark()        
