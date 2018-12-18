# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:01:04 2018

@author:mag
"""
#Define  a  function  game  that  takes  no  arguments.  It  should  play  as  many
#rounds  of  a  simple  dice  game  as  the  user  wants.  Each  round  should 
#require the user to enter “odd”, “even”, or “quit”. The game then produces two
#dice  values  randomly  between  1  and  6,  adds  them  together,  and determines
#whether  the  result  is  odd  or  even.  If  the  user  correctly predicted  the  
#oddness  or  evenness  then  it  should  print  “You  win!”, otherwise  it  should  
#print  “Sorry,  you  lose!”.  This  should  continue  until  the user types “quit”.
from random import randint

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

