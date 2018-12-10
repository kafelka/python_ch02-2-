# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 14:05:18 2018

@author: nahas
"""
#ex11

#print("How old are you?", end=" ")
#age = input()
#print("How tall are you?", end = " ")
#height = input()
#print("How much do you weigh?", end= " ")
#weight = input()
#
#print(f"So, you're {age} years old, {height} tall and {weight} heavy.")

print("****************")

#ex12

#age = input("How old are you? ")
#height = input("How tall are you? ")
#weight = input("How much do you weigh? ")
#
#print(f"So, you're {age} years old, {height} tall and {weight} heavy.")

#ex13

from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

#cd to the directory of the file and
#run the anaconda prompt and type in python LPTHW_ex11to17.py abc def ghi