# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:51:11 2018

@author: mag
"""

from random import randint

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