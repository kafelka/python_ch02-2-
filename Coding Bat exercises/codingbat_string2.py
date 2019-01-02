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

#Return the number of times that the string "hi" appears anywhere 
#in the given string.
#count_hi('abc hi ho') → 1
#count_hi('ABChi hi') → 2
#count_hi('hihi') → 2

#def count_hi(str):
#    count = 0
#    for i in range(len(str)-1):
#        if str[i] == "h" and str[i+1] =="i":
#            count = count + 1
#    return count

def count_hi(str):
    return str.count("hi")

print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))
############################
print("\n")

#Return True if the string "cat" and "dog" appear the same number 
#of times in the given string.
#cat_dog('catdog') → True
#cat_dog('catcat') → False
#cat_dog('1cat1cadodog') → True

#def cat_dog(str):
#    countDog = 0
#    countCat = 0
#    for i in range(len(str)-2): 
#        if str[i] == "c" and str[i+1] == "a" and str[i+2] == "t":
#            countCat += 1
#        
#        elif str[i] == "d" and str[i+1] == "o" and str[i+2] == "g":
#            countDog += 1
#            
#    if countDog == countCat:
#        return True
#    else:
#        return False
    
def cat_dog(str): 
    return str.count("cat") == str.count("dog")
    

print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))
############################
print("\n")


#Return the number of times that the string "code" appears anywhere 
#in the given string, except we'll accept any letter for the 'd', so 
#"cope" and "cooe" count.
#count_code('aaacodebbb') → 1
#count_code('codexxcode') → 2
#count_code('cozexxcope') → 2

def count_code(str):
    count = 0
    for i in range(len(str)-3): 
        if str[i:i+2] == "co" and str[i+3] == "e":
            count += 1
    return count

print(count_code('aaacodebbb'))
print(count_code('codexxcode'))
print(count_code('cozexxcope'))
print("\n")

#Given two strings, return True if either of the strings appears at the 
#very end of the other string, ignoring upper/lower case differences (in other 
#words, the computation should not be "case sensitive"). Note: s.lower() returns 
#the lowercase version of a string.
#end_other('Hiabc', 'abc') → True
#end_other('AbC', 'HiaBc') → True
#end_other('abc', 'abXabc') → True

def end_other(a, b):
    a = a.lower()
    b = b.lower()
    
    return a.endswith(b) or b.endswith(a)
    
print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))
print("\n")

#Return True if the given string contains an appearance of "xyz" where 
#the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" 
#does not.
#xyz_there('abcxyz') → True
#xyz_there('abc.xyz') → False
#xyz_there('xyz.abc') → True

def xyz_there(str):
    for i in range(len(str)-2):
        if str[i] != "." and str[i+1:i+3] == "xyx":
             return True
    return False

print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc'))
print("\n")