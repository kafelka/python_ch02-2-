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
print(jason.balance)
print(jason.name)
print(jason.age)

jason.withdraw(100.0)
print("Checking balance after withdrawing cash:")
print(jason.balance)
#jason.withdraw(1000.0)
jason.deposit(800.0)
print("Checking balance after deposit cash:")
print(jason.balance)

maggie = Customer("Maggie K.", 2000.0)
print(maggie.balance)
print(maggie.name)
print(maggie.age)
maggie.withdraw(200.0)

#cos mi tu nie dziala:
#withdrawAmount = float(input("How much did you withdraw today?"))
#print(maggie.withdraw(withdrawAmount))

name1 = "Clare B"
balance1 = 3000.0

print("Type:", type(jason))

print(list(range(10)))

print(list(range(1,10)))

print(list(range(1,10,3)))


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

