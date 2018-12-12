# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 12:16:04 2018

@author: nahas
"""
my_fav_fruit = ["apple", "raspberry", "grapefruit"]
print(my_fav_fruit)
print(my_fav_fruit[0])

x = ["this", 55, "that", my_fav_fruit]
print(x)
print(x[0])
print(x[1])
print(x[3])
print(x[3][0])
#print(x[4])

print("*******************")
x.remove(my_fav_fruit)
print(x)
x[1] = "and"   #replacing/overwriting/updating item with index 1
print(x)

x.append("again") #appending/extending
print(x)

a = [0, 2, 3, 2] #removes the first matching value (not returning)
a.remove(2)
print(a)

b = [3, 2, 2, 1] # removes the item at a specific index (not returning)
del b[1]
print(b)

c = [4, 3, 5]  #removes the item at a specific index and returns it
c.pop(1)
print(c)

d = [1, 2, 3, 4, 5, 6]
del d[2:]
print(d)

print("*******************")
e = ["the", "cat", "sat"]
f = ["on", "the", "mat"]
g = e + f
print(g)

h = 2 * e
print(h)
print("*******************")
print(set(e+f))

