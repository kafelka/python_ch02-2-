# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 15:09:58 2018

@author: nahas
"""

phoneBook = {"Joan": ("753", 13, "NW3 5GH", "London", 34),
             "Edi": ("225", 7, "AB10 1EZ", "Aberdeen", 28),
             "Natalie": ("477", 5, "L1 0RD", "Liverpool", 26),
             "Veronica": ("850", 21, "M1 1FR", "Manchester", 30)
             }


def addToPhoneBook():
    name = input('What is your first name? ')
    last3DigitNo = input('What are the last three digit of your phone no.? ')
    luckNo = int(input('What is your lucky no.? '))
    postCode = input('What is your post code? ')
    townCity = input('Which city do you come from? ')
    age = input("How old are you? ")
    return {name: (last3DigitNo, luckNo, postCode, townCity, age)}



#newEntry = addToPhoneBook()
newEntry = {}
phoneBook.update(newEntry)
print("The phone book has been successfully update with the new record: ", newEntry)
print(phoneBook)

def sortByName():
    sortBy = sorted(phoneBook.items(), key=lambda kv:kv[0])
    print("\nPhone book sorted by \n", sortBy)
    
def sortByCity():
    sortBy = sorted(phoneBook.items(), key=lambda kv:kv[1][3])
    print("\nPhone book sorted by \n", sortBy)

def sortByLuckyNo():
    sortBy = sorted(phoneBook.items(), key=lambda kv:kv[1][1])
    print("\nPhone book sorted by \n", sortBy)
    
sortByName()
sortByCity()
sortByLuckyNo()