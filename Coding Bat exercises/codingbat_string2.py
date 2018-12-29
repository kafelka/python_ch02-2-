#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 23:36:15 2018

@author: kafelka
Coding Bat String 2 exercises
"""
#Given a string, return a string where for every char in the original, 
#there are two chars.
#double_char('The') → 'TThhee'
#double_char('AAbb') → 'AAAAbbbb'
#double_char('Hi-There') → 'HHii--TThheerree'

def double_char(str):
    newStr = ""
    for i in str:
        newStr = newStr + i * 2
    return newStr
    
    
print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))
############################
print("\n")


############################
print("\n")


############################
print("\n")