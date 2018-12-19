# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:09:06 2018

@author: mag
"""
from random import randint

#ex1 repeated division
x = 33
while x >= 1:
    print(x, ": ", end=' ')
    x = x / 2  
print(x)

#n + (n-1) +...+ 2 + 1

#ex2 triangular numbers
def triangular(n):
    numx3 = 0
    while n > 0:
        numx3 = numx3 + n
        n = n - 1
    return numx3

print(triangular(1))   
print(triangular(2))
print(triangular(3))
print(triangular(4))
print(triangular(5))
print(triangular(6))

#ex3 student marks
mark = 1
while mark > 0:
    mark = int(input("What's your mark: "))
    print("Your mark is", mark, end = ". ")
    if mark >= 70:
        print("First class!")
    elif mark >= 40:
        print("Pass!")
    else:
        print("Oh no, that's a fail...")  

print("***********************") 
i = 55
while i > 10:
    print(i)
    i = i * 0.8
    if i == 35.2:
        break


#ex4 break statement in a while loop
while True:
    name = input("What's your name? ")
    if name == "done":
        break
    print("Hello", name)
    
#ex5 guessing game 
    
    def guess(attempts, intrange):
    number = randint(1, intrange)
    print("Welcome! Can you guess my secret number? ")
    
    while attempts > 0:
        print(f"You have {attempts} attempts left.")
        guess = int(input("Take a guess! "))
        
        if guess > number:
            print("No, too high!")
        elif guess < number:
            print("No, too low!")
        else:
            print("Well done. You got it right!")
            
            break
        
        print("Game over! Thanks for playing!")
        attempts = attempts - 1
        
guess(4,10)
    
    
    
#ex6 dice game 

def guess(attempts, intrange):
    number = randint(1, intrange)
    print("Welcome! Can you guess my secret number? ")
    
    while attempts > 0:
        print(f"You have {attempts} attempts left.")
        guess = int(input("Take a guess! "))
        
        if guess > number:
            print("No, too high!")
        elif guess < number:
            print("No, too low!")
        else:
            print("Well done. You got it right!")
            
            break
        
        print("Game over! Thanks for playing!")
        attempts = attempts - 1
        
guess(4,10)
       
#rounds  of  a  simple  dice  game  as  the  user  wants.  Each  round  should 
#require the user to enter “odd”, “even”, or “quit”. The game then produces two
#dice  values  randomly  between  1  and  6,  adds  them  together,  and determines
#whether  the  result  is  odd  or  even.  If  the  user  correctly predicted  the  
#oddness  or  evenness  then  it  should  print  “You  win!”, otherwise  it  should  
#print  “Sorry,  you  lose!”.  This  should  continue  until  the user types “quit”.


def sumDice():
    diceResult = (randint(1,6) + randint(1,6))
    if diceResult % 2 == 0:
        return "even"
    else:
        return "odd"
    
def diceGame():
    userGuess = ""
    while userGuess != "quit":
        userGuess = input("Guess the result of dice game? Type odd, even or quit: ")
        diceResult = sumDice()

        if userGuess == 'quit':
            print('Thanks, bye!')
            break
        elif userGuess == diceResult:
            print("You win!")
#        elif userGuess != diceResult:
#            print("You lose!")
        else:
            print("You lose!")
#        else:
#           print('system error')
            
diceGame()    
    
    
    