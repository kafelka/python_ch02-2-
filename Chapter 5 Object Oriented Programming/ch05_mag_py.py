# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:07:41 2018

@author: maggie
"""
#ex1 using classes

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
print(jason.balance)
print(jason.name)
print(jason.age)

jason.withdraw(100.0)
print("Checking balance after withdrawing cash:")
print(jason.balance)
jason.withdraw(500.0)
jason.deposit(800.0)
print("Checking balance after deposit cash:")
print(jason.balance)

maggie = Customer("Maggie K.", 2000.0)
print(maggie.balance)
print(maggie.name)
print(maggie.age)
maggie.withdraw(200.0)


withdrawAmount = float(input("How much did you withdraw today?"))
print(maggie.withdraw(withdrawAmount))

name1 = "Clare B"
balance1 = 3000.0

print("Type:", type(jason))
print(list(range(10)))
print(list(range(1,10)))
print(list(range(1,10,3)))

#ex2 & 3 using inheritance

class Animal():
    def eat(self):
        print("Yum yum yum!")
        
class Dog(Animal):
    def bark(self):
        print("Woof, woof!")
        
class Cat(Animal):
    def meow(self):
        print("Meooow!")
    def paws(self):
        print("I've got 4 paws.")
        
Snoopy = Dog()
Snoopy.bark()
Snoopy.eat()

Cosmo = Cat()
Cosmo.meow()
Cosmo.paws()
Cosmo.eat()

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
            print('stranger coming!!!')
        
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

#using association

import sys

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def eat(self):
         print('yum')
         
class Dog(Animal):
    def bark(self):
        print('Woof!')
        
class Robot():
    def move(self):
            print('...move move move...')
class CleanRobot(Robot):
    def clean(self):
        print('I vacuum dust')
        
class SuperRobot():
    def __init__(self,name,age):
        #This class contains 3 objects'
        self.name = name
        self.age = age
        
        self.o1 = Robot()
        self.o2 = Dog(name,age)
        self.o3 = CleanRobot()
        
    def playGame(self):
        print('alphago game')
        
    def move(self):
        return self.o1.move() #using robot class method
    
    def bark(self):
        return self.o2.bark() #using dog class method
    
    def eat(self):
        return self.o2.eat() #using dog class method
    
    def clean(self):
        return self.o3.clean() #using cleanrobot method
    
#input('pet\'s name: ')
name = sys.argv[1] 
#int(input('pet\'s age: '))
age = sys.argv[2] 

print(name)
print(age)

machineDog = SuperRobot(name, age)
machineDog.move()
machineDog.bark()
machineDog.eat()



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
    def __init__(self, name, motivation=0):
        Human.__init__(self, name)
        self.motivation = motivation
        
        
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
    person = NonClimber(name)
    print("This part has not been finished yet.")

