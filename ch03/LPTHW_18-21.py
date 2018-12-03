# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:55:43 2018

@author: nahas
"""
##ex18)
#def print_two(*args):
#    arg1, arg2 = args
#    print(f"arg1: {arg1}, arg2: {arg2}")
#    
#def print_two_again(arg1, arg2):
#    print(f"arg1: {arg1}, arg2: {arg2}")
#    
#def print_one(arg1):
#    print(f"arg1: {arg1}")
#    
#def print_none():
#    print("I got nothing'.")
#    
#print_two("mag", "gamon")
#print_two_again("zero", "one")
#print_one("First!")
#print_none()
#
#print("\n")
##ex19
#
#def cheese_and_crackers(cheese_count, boxes_of_crackers):
#    print(f"You have {cheese_count} cheeses!")
#    print(f"You have {boxes_of_crackers} boxes of crackers!")
#    print("Man, that's enough for a party!")
#    print("Get a blanket.\n")
#    
#print("We can just give the function numbers directly:")
#cheese_and_crackers(20,30)
#
#print("OR, we can use variables from our script:")
#amount_of_cheese = 10
#amount_of_crackers = 50
#
#cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#
#print("We can even do math inside too:")
#cheese_and_crackers(10+20, 5+6)
#
#print("And we can combine the two, variables and math:")
#cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("\n")
#ex20

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())
    
def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print(line_count, f.readline())
    
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

currrent_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)


print("\n")
#ex21