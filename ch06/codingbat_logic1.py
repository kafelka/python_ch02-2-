# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 21:06:14 2018

@author: nahas
"""
#CodingBat Logic1 exercises

#When squirrels get together for a party, they like to have cigars. 
#A squirrel party is successful when the number of cigars is between 40 and 60, 
#inclusive. Unless it is the weekend, in which case there is no upper bound on 
#the number of cigars. Return True if the party with the given values is successful, 
#or False otherwise.
#
#cigar_party(30, False) → False
#cigar_party(50, False) → True
#cigar_party(70, True) → True

def cigar_party(cigars, is_weekend):
    if is_weekend is True and cigars >= 40: 
        return True
    elif (cigars >= 40 and cigars <= 60):
        return True
    else:
        return False
    
print(cigar_party(30, True))
print(cigar_party(50, False))
print(cigar_party(70, True))

############################
print("\n")


#You and your date are trying to get a table at a restaurant. The parameter 
#"you" is the stylishness of your clothes, in the range 0..10, and "date" is the 
#stylishness of your date's clothes. The result getting the table is encoded as an 
#int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, 
#then the result is 2 (yes). With the exception that if either of you has style 
#of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
#
#date_fashion(5, 10) → 2
#date_fashion(5, 2) → 0
#date_fashion(5, 5) → 1

def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1

print(date_fashion(5, 10))
print(date_fashion(5, 2))
print(date_fashion(5, 5))

############################
print("\n")

#The squirrels in Palo Alto spend most of the day playing. In particular, 
#they play if the temperature is between 60 and 90 (inclusive). Unless it is 
#summer, then the upper limit is 100 instead of 90. Given an int temperature and 
#a boolean is_summer, return True if the squirrels play and False otherwise.
#
#squirrel_play(70, False) → True
#squirrel_play(95, False) → False
#squirrel_play(95, True) → True

def squirrel_play(temp, is_summer):
    if temp >= 60 and temp <= 90:
        return True
    elif is_summer == True and (temp >= 60 and temp <= 100):
        return True
    else:
        return False
 
print(squirrel_play(70, False))
print(squirrel_play(95, False))
print(squirrel_play(95, True))
print(squirrel_play(55, True))
    
############################
print("\n")