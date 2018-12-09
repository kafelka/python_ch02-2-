# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:05:35 2018

@author: nahas
"""
#CodingBat WarmUp2 exercises

#Given a string and a non-negative int n, return a larger string that is 
#n copies of the original string.
#string_times('Hi', 2) → 'HiHi'
#string_times('Hi', 3) → 'HiHiHi'
#string_times('Hi', 1) → 'Hi'

def string_times(str, n):
  return str * n

print(string_times("Hiya!", 2))

############################
print("\n")


#Given a string and a non-negative int n, we'll say that the front of the 
#string is the first 3 chars, or whatever is there if the string is less
# than length 3. Return n copies of the front;
#front_times('Chocolate', 2) → 'ChoCho'
#front_times('Chocolate', 3) → 'ChoChoCho'
#front_times('Abc', 3) → 'AbcAbcAbc'

def front_times(str, n):
    return n * str[:3]

print(front_times("Juice", 4))

############################
print("\n")

#Given a string, return a new string made of every other char starting with 
#the first, so "Hello" yields "Hlo".
#string_bits('Hello') → 'Hlo'
#string_bits('Hi') → 'H'
#string_bits('Heeololeo') → 'Hello'

def string_bits(str):
    result = ""
    for n in range(len(str)):
        if n % 2 == 0:
            result = result + str[n]
    return result

print(string_bits("Python"))

############################
print("\n")