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
    print("\nPhone book sorted by name:\n", sortBy)
    
def sortByCity():
    sortBy = sorted(phoneBook.items(), key=lambda kv:kv[1][3])
    print("\nPhone book sorted by city:\n", sortBy)

def sortByLuckyNo():
    sortBy = sorted(phoneBook.items(), key=lambda kv:kv[1][1])
    print("\nPhone book sorted by lucky no:\n", sortBy)

def sortByAge():
    sortBy = sorted(phoneBook.items(), key=lambda kv:kv[1][4])
    print("\nPhone book sorted by age:\n", sortBy)
       
sortByName()
sortByCity()
sortByLuckyNo()
sortByAge()

def queensAgeDifference():
    queensAge = (2018 - 1926)
    for name in phoneBook.keys():
        userAge = phoneBook[name][4]
        difference = queensAge - userAge
        print(f"\nThe difference between {name}'s age and queen's age is: \n", difference)
    
queensAgeDifference()

def printPhoneBookToFile(dictionary):
# with guarantees closing of the resource (the variable after "as")
# after the program continues outside the with block
    with open('phoneBook.txt', 'w') as f:
        f.write(str(dictionary))

#printPhoneBookToFile(phoneBook)   
    