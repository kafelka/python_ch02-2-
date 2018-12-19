# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 15:09:58 2018

@author: mag
"""
phoneBook = {}
#phoneBook = {"Joan": ("753", 13, "NW3 5GH", "London", 34),
#             "Eddie": ("225", 7, "AB10 1EZ", "Aberdeen", 28),
#             "Natalie": ("477", 5, "L1 0RD", "Liverpool", 26),
#             "Veronica": ("850", 21, "M1 1FR", "Manchester", 30)
#             }

x = (len(phoneBook)-1)
while (x) < 3:       
       name = input('What is your first name? ').title()
       last3DigitNo = input('What are the last three digit of your phone no.? ')
       luckNo = int(input('What is your lucky no.? '))
       postCode = input('What is your post code? ').upper()
       townCity = input('Which city do you come from? ').title()
       age = int(input("How old are you? "))

       phoneBook[name] = (last3DigitNo, luckNo, postCode, townCity, age)
       
       print(phoneBook)
       x = (len(phoneBook)-1)
       print(x)  
    
def addToPhoneBook():
    name = input('What is your first name? ').title()
    last3DigitNo = input('What are the last three digit of your phone no.? ')
    luckNo = int(input('What is your lucky no.? '))
    postCode = input('What is your post code? ').upper()
    townCity = input('Which city do you come from? ').title()
    age = int(input("How old are you? "))
    return {name: (last3DigitNo, luckNo, postCode, townCity, age)}

#newEntry = addToPhoneBook()
##newEntry = {}
#phoneBook.update(newEntry)
#print("The phone book has been successfully update with the new record: ", newEntry)
#print(phoneBook)

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
    
def sortByChoice():
    choice = input("""
What would you like to print the phone book by?
Select:
   * 1 for sorting by name
   * 2 for sorting by city
   * 3 for sorting by lucky number
   * 4 for sorting by age\n """)
        
    if choice == "1":
        sortByName()
    elif choice == "2":
        sortByCity()
    elif choice == "3":
        sortByLuckyNo()
    else:
        sortByAge()
        
sortByChoice()       

#def queensAgeDifference():
#    queensAge = (2018 - 1926)
#    for name in phoneBook.keys():
#        userAge = phoneBook[name][4]
#        difference = queensAge - userAge
#        print(f"\nThe difference between {name}'s age and queen's age is: \n", difference)
#    
#queensAgeDifference()

def queen():
    queensAge = (2018 - 1926)
    colleagues = ", ".join(list(sorted(phoneBook)))
    selectName = input(f"Type name of your colleague in order to find the difference in age between then and the Queen. List of colleagues: {colleagues}: \n") 
    userAge = phoneBook[selectName][4]
    result = queensAge - userAge
    print(f"The age difference between the Queen and {selectName} is: {result}.")

queen()

def printPhoneBookToFile(dictionary):
# with guarantees closing of the resource (the variable after "as")
# after the program continues outside the with block
    with open('phoneBook.txt', 'w') as f:
        f.write(str(dictionary))

#printPhoneBookToFile(phoneBook)   
    