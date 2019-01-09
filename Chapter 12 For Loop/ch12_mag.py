# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:16:58 2018

@author: maggie
"""
#ex1 loop through a list
my_shopping_cart = ["cake", "plates", "plastic forks", "juice", "cups"]
for item in my_shopping_cart: 
    print(item)


#ex2 updating list values
values = [875, 23, 451]

for val in values:
    print("--->" + str(val))
    
for val in values:
    print("--->" + str(val + 50))

for val in values:
    print("--->" + str(val))
    print("--->" + str(val + 50))

##ex3 create list and print
values = ["this", 55, "that"]
for item in values:
    print("***", item)
  
##ex4 loop through strings
for char in "Yes":
    print(char)
    
for char in "I am a cat.".split():  #to divide by words
    print(char)  
    
for char in "I am a cat.".split("a"):  #to divide by words, omit "a"
    print(char)    
    
for char in "I-am-a-cat.".split("-"):  #omit "-"
    print(char)    
      
#ex5  loop through a tuple
#birds = ("tucan", "paradise bird", "owl")
#
#for item in tuple:
#    print("***", item)
    
#'type' object is not iterable so the above example would have an error

#ex6&7 loop through dictionary data type
        
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
    
#ex8?? combine counting loop and conditionals to filter out values
densities = {"iron":(7.8, 5, 1000), "gold":(19.3, 20, 2), "zinc":(7.13, 10, 50), "lead": (11.4, 8, 40)}
metals = list(densities.keys())
metals.sort(reverse = True, key=lambda m:densities[m])

keyValues = sorted(densities.items(), key=lambda kv:kv[1][1], reverse=True)

for metal in metals:
    if densities[metal][0]>10:
        print(metal, densities[metal][0])
    
#ex9 design a sum function 
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
#loopRound = 1  
#for gift, item in gifts.items():
#    print("open box", loopRound, "the gift is", gift)
#    print("the item is", item)
#    if item >= 3:
#        print("Nice, I have received", item, "of", gift)
#    else:
#        print("Please give me more of", gift)
#        
#    loopRound += 1
#    
#    
#    for gift in gifts:
#        print("open box" loopRound, "the git is", gift)
#        print("the item is", gifts[gift])
    
#print(len("magdalena"))
#print(list(range(10)))
#print(list(range(1,10)))
#print(list(range(1,10,2)))

#ex10 looping with index values 
values = [3,12,9]
for index in range(len(values)):
    values[index] = values[index] ** 2
print(values)

for i in range(3,10,2):
    print(i)
      
print(list(range(3)))
print(type(range(3)))

values = [3, 12, 9, 5, 6]
for index in range(1, len(values), 2):
    print(values[index], "with index", index)
    values[index] = values[index] ** 2
    
values = [3,12,9]
for index in range(len(values)):
    print(index)
    values[index] = values[index] * 2
print(values)

#ex11 using a loop with the range function
names = ["milly", "bob", "kate", "mary", "alanis", "elly"]
for i in range(1, len(names), 3):
    print("find them", names[i])
        

#ex12 using breaks in for loops
nums = [1,5,30,200,101,100,22]
for n in nums:
    if n > 100:
        print("found", n)
        break
    
nums = [1,5,30,200,101,100,22]
print("length",len(nums))
print(list(range(len(nums))))
for index in range(len(nums)):
    if nums[index] > 100:
        print("break:", nums[index], "with index", index)
        break
    
nums = [1,5,30,200,101,100,22]
for index in range(len(nums)):
    print("loop index", index, "with value", nums[index])
    if nums[index] > 100:
        print("break:", nums[index], "with index", index)
        break
print("**************")
nums = [1,5,30,200,101,100,22]
for index in range(len(nums)):
    print("loop index", index, "with value", nums[index])
    if nums[index] > 100:
        print("need to break:", nums[index], "with index", index)
    else:
        print("Oh, you forgot to break the loop", nums[index], "with index", index)
        

colours = ["red", "green", "red", "green", "blue", "green", "green"]
d = {}
for item in colours:
    
    if item not in d:
        d[item] = 1
        print(d, "first time")
        
    else: 
        d[item] = d[item] + 1
        print(d)
    
    
#ex13 creating nested loops
outer_vals_list = [1, 2, 3]
inner_vals_list = ["A", "B", "C"]
dict = {}

for outer_val in [1, 2, 3]:
#    print(outer_val)
    for inner_val in ["A", "B", "C"]:
#        print(inner_val)
        dict[outer_val] = inner_val
        print(dict)


#for i in range(1,7):
#    for j n range(1,11):
#        print("{0:})


# Ex14: Multiplication table with a for loop

for i in range(1,11):
   for j in range(1,11):
       print('{0:>3}'.format(i*j), end='')
   print('\n')

# VERSION 2

table = int(input("Please enter a times table: "))
for x in range(0, 5):
   print(x, "x", table, "=", x*table)