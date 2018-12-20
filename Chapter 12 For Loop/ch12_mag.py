# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:16:58 2018

@author: maggie
"""
#ex1
my_shopping_cart = ["cake", "plates", "plastic forks", "juice", "cups"]
for item in my_shopping_cart: 
    print(item)

#ex2 
values = [875, 23, 451]

for val in values:
    print("--->" + str(val))
    
for val in values:
    print("--->" + str(val + 50))

for val in values:
    print("--->" + str(val))
    print("--->" + str(val + 50))

#ex3
values = ["this", 55, "that"]
for item in values:
    print("***", item)
  
#ex4
for char in "Yes":
    print(char)
    
for char in "I am a cat.".split():  #to divide by words
    print(char)  
    
for char in "I am a cat.".split("a"):  #to divide by words, omit "a"
    print(char)    
    
for char in "I-am-a-cat.".split("-"):  #omit "-"
    print(char)    
      
#ex5  
#birds = ("tucan", "paradise bird", "owl")
#
#for item in tuple:
#    print("***", item)
    
#'type' object is not iterable !!!
        
#salary = {"al":20000, "bo":50000, "ced":1500}
#salaryKeys = list(salary.keys())
#salaryValues = list(salary.values())

metals = {
        "gold": (19320, 40.81, 10),
        "silver": (10490, 0.53, 100),
        "platinum": (21400, 1, 1)
        }

print(metals)

metalKeys = list(metals.keys())
metalValues = list(metals.values())

print("list keys", metalKeys)
print("list values", metalValues)

for i in metalKeys:
    print("keys",i)
    
for n in metalValues:
    print("values",n)
    
for key, value in metals.items():
    print("the KV pair:", key, value)
    
x = sorted(metals.items(), key=lambda kv:kv[1][1])
print("sort by second value:", x)

for key, value in x:
    print(key, value)
    
#metalValues.sort(reverse = True, key=lambda m:metals[m])
#keyValue = sorted(densities.items(), key=lambda kv:kv[1][1], reverse = True)
#
#for metal, metalValue in keyValue:
#    print(metal, metalValue)
    
densities = {"iron":(7.8, 5, 1000), "gold":(19.3, 20, 2), "zinc":(7.13, 10, 50), "lead": (11.4, 8, 40)}
metals = list(densities.keys())
metals.sort(reverse = True, key=lambda m:densities[m])

keyValues = sorted(densities.items(), key=lambda kv:kv[1][1], reverse=True)
for metal in metals:
    if densities[metal][0]>8:
        print('{0:>8} = {1:5.1f}'.format(metal, densities[metal][0]))
    
#ex8???
densities = {"iron":(7.8, 5, 1000), "gold":(19.3, 20, 2), "zinc":(7.13, 10, 50), "lead": (11.4, 8, 40)}
metals = list(densities.keys())
metals.sort(reverse = True, key=lambda m:densities[m])

keyValues = sorted(densities.items(), key=lambda kv:kv[1][1], reverse=True)

for metal in metals:
    if densities[metal][0]>10:
        print(metal, densities[metal][0])
    
#ex9
values = [3,12,9]
total = 0
for val in values:
    total += val
print("Total:" + str(total))    
    

def sumValues(I):
    sumV = 0
    for val in I:
        sumV += val
    return sumV

print(sumValues(values))


valuesList = [3,12,9]
total = 0
for value in valuesList:
    print("Before adding", value, "total is", total)
    total = value + total
    print("After adding", value, "total is", total)
    
print("Total:", str(total))

gifts = {
        "socks": (6, 15, "green"),
        "tea": (2, 5, "cherry"),
        "chocolates": (4, 5, "almond"),
        "books": (5, 10, "fiction")
        }
loopRound = 1  
for gift, item in gifts.items():
    print("open box", loopRound, "the gift is", gift)
    print("the item is", item)
    if item >= 3:
        print("Nice, I have received", item, "of", gift)
    else:
        print("Please give me more of", gift)
        
    loopRound += 1
    
#    
#    for gift in gifts:
#        print("open box" loopRound, "the git is", gift)
#        print("the item is", gifts[gift])