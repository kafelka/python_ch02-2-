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

#from sys import argv
#
#script, first, second, third = argv
#
#print("The script is called:", script)
#print("Your first variable is:", first)
#print("Your second variable is:", second)
#print("Your third variable is:", third)

#cd to the directory of the file and
#run the anaconda prompt and type in python LPTHW_ex11to17.py abc def ghi

print("****************")

#ex14
from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.   
""")

