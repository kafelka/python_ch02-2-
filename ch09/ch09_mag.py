# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 12:16:04 2018

@author: nahas
"""
#my_fav_fruit = ["apple", "raspberry", "grapefruit"]
#print(my_fav_fruit)
#print(my_fav_fruit[0])
#
#x = ["this", 55, "that", my_fav_fruit]
#print(x)
#print(x[0])
#print(x[1])
#print(x[3])
#print("****** result for x[-1][-2]:")
#print(x[-1][-2])
#print("result of [x[-2][-3]]:")
#print(x[-2][-3])
#print(x[3][0])
#
#print("result of x[-1][-2][-2][0]")
#print(x[-1][-2][-2][0])
##print(x[4])
#
#print("*******************")
#print("print x before removal: ", x)
#x.remove(my_fav_fruit)
#print("print x after removal:", x)
#x[1] = "and"   #replacing/overwriting/updating item with index 1
#print(x)
#
#x.append("again") #appending/extending the list ( as last element)
#print(x)
#y = x
#y = x.append("hello")
#print(y)
#print(type(y))
#print(x)
#
#a = [0, 2, 3, 2] #removes the first matching value (not returning)
#a.remove(2)
#print(a)
#
#b = [3, 2, 2, 1] # removes the item at a specific index (not returning)
#del b[1]
#print(b)
#
#c = [4, 3, 5]  #removes the item at a specific index and returns it
#c.pop(1)
#print(c)
#
#d = [1, 2, 3, 4, 5, 6]
#del d[2:]
#print(d)
#
#print("operations*******************")
#e = ["the", "cat", "sat"]
#f = ["on", "the", "mat"]
#g = e + f
#print(g)
#
#h = 2 * e
#print(h)
#print("*******************")
#print(set(e+f))
#
#print("set **********")
#print("print set(e): ", set(e))   #printing in curly brackets dictionary
#a = set(e)
#print("print a:", a)
#
#print("*****slicing******")
#k = ["this", "and", "that", "once", "again"]
#print(k)
#print(k[1:4])
#print(k[0:0])
#print(k[0:2])
#print(k[3:5])
#print(k[-1:-3])
#print(k[-3:-1])
#print(k[-3:])
#print(k[-5:-2])
#print(k)
#
#z = ["the", "cat", "sat", "on", "the", "mat"]
#print(z[3:10])
#print(z[8:10])

#
#print("*****sorting******")
#m = [7,11,3,9,2]
#print("print m:", m)
#n = sorted(m)
#print("print m: ", m)
#print("print n: ", n)
#
#m.sort()
#print("print m after m.sort: ", m)
#print("*******************")
#
#zz = ["ok", "cs", "yw", "zs", "hd"]
#print("print original zz :", zz)
#yy = sorted(zz)
#print(yy)
#print(zz)
#zz.sort()
#print("print zz after zz.sort(): ", zz)
#print(zz.sort())
#
#print("*******************")
#r = [7,11,3,9,2]
#print("print original r: ", r)
#print(sorted(r))
#
#sorted(r,reverse = True) #reversing changes
#print(r)
#
#rr = [7,11,3,9,2]
#print("print original rr: ", rr)
#rr.sort()
#print("print rr after rr.sort: ", rr)
#
#rr.sort(reverse = True)
#print("print reversed rr: ", rr)
#print("\n")
#
#print("REVERSE generic sorted() function")
#aaa = ["ab", "cs", "yw", "zs", "hd"]
#aa2 = sorted(aaa, reverse = True)
#print("after sorted(aaa) st is =:", aaa)
#print("aa2 = sorted(aaa) is =:", aa2)
#
#print("object method .sort() , the same in memory")
#print("original aaa: ", aaa)
#aaa.sort(reverse = True)
#bbb = aaa.sort()
#print("now aaa is =:", aaa)
#print("now aa2 is =:", aa2)
#
#print("\n")
#print("generic sorted() function")
#st = ["ab", "cs", "yw", "zs", "hd"]
#st2 = sorted(st)
#print("after sorted(st) st is =:", st)
#print("st2 = sorted(st) is =:", st2)
#
#print("object method .sort() , the same in memory")
#print("original st: ", st)
#st.sort()
#bb = st.sort()
#print("now st is =:", st)
#print("now st2 is =:", st2)


#print("****tuples-immutable=read from them but cannot change****")
#print("example 1")
#a = [0,1,2,3,4,5,6,7,8,9]
#print(a)
#del a[-1]
#print(a)
#del a[-3]
#print(a)
#del a[-3:]
#print(a)
#
#b = (0,1,2,3,4,5,6,7,8,9)
##del b[-1]  tuple object does not support item deletion
#print(b)
#
#print("\n")
#print("example 2")
#a = [0,1,2,3,4,5,6,7,8,9]
#a[0] = 50
#print(a)
#
#b = (0,1,2,3,4,5,6,7,8,9)
##b[0] = 50 tuple object does not support item assignment
#print(b)
#
#print("\n")
#print("example 3")
#a.append("z")
#print(a)
#
##b.append("z") #tuple object has no attribute 'append'
#print(b)
#
#c = list(b)
#print(type(b))
#print(type(c))

#dokonczyc pozniej
#z = sorted(a, reverse = True)
#if a == b:
#    print(True)
#else:
#    print(False)

print("\n")
print("*******lambda******")

a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
myFavF = ["apple", "orange", "banana"]
x = ["xa", "sb", "lf", "hw", "ed", "fy"]
z = ["fg", "uj", "sx", "uj", "ww", "cf"]
y = sorted(x)

y[0] = "zz"
x2 = [("a", 3 ,z), ("c", 1 ,y), ("b", 5, x)]

print(x2)
print("*****")
print(sorted(x2, key=lambda s:s[2][-1][-2]))
print("*****")
#print("z is ", z)
#print("y is ", y)
#print("x is ", x)

print("*****")
print(sorted(x2, key=lambda s:s[1]))
#[('c', 1, ['ed', 'fy', 'hw', 'lf', 'sb', 'xa']), 
# ('a', 3, ['fg', 'uj', 'sx', 'uj', 'ww', 'cf']), 
# ('b', 5, ['xa', 'sb', 'lf', 'hw', 'ed', 'fy'])]
print("*****")
print(sorted(x2, key=lambda s:s[2]))
print("*****")
#print(sorted(x2, key=lambda s:s[2][1]))

#a = [1,2,3,4]
#b = [3,4,10,3]
#c = [20,10,30,40]
#
#y2 = [("a", 3 ,c), ("c", 1 ,b), ("b", 5, a)]
#
#print(sorted(y2, key=lambda s:s[1]))
#print("*****")
#print(sorted(y2, key=lambda s:s[2]))
#print("*****")
#print(sorted(y2, key=lambda s:s[2][-1]))

print("******new example*******")

a = [0,1,2,3,4,5,6,7,8,9]
b = [0,1,2,3,4,5,6]
c = [2,2,3,3,4,5,6,7,8,9]

myFavF = ["apple", "orange", "banana"]
x = ["lf", "sb", "hw", "hw", "aa", "ed", "fy"]
z = ["uj", "fg", "uj", "ww", "sx", "cf"]

y = sorted(x)
y[0] = "zz"
y[-2] = "sd"
# ['zz', 'ed', 'fy', 'hw', 'hw', 'sd', 'sb']
x2 = [(a, 3, "a", z), (c, 1, "c", y), (b, 5, "b", x)]

print("x2 ")
print(x2)
print("***")
print(sorted(x2, key=lambda s:s[0][-3]))
print("*****")
print(sorted(x2, key=lambda s:s[3][-3][-2]))
print("*****")
print(sorted(x2, key=lambda s:s[3][-3][-2])[0])

print("Ellen's example")

employees = [('Janine Saunders', 50000, 'UX Designer'),
     ('Robert Webster', 90000, 'Senior Engineer'),
     ('Jack Murning', 40000, 'Junior Web Developer'),
     ('Jen Burns', 30000, 'Content Creator'), 
     ('Hannah Beth', 40000, 'Communications Specialist')]
    
print (sorted(employees, key = lambda salary:salary[2]))





#x = ["the", "cat", "on"]
#y = [7,11,3,9,2]
#z = [2,3,7,8,11]
#x2 = [("a",3,z), ("c",1,y), ("b",5,x)]
#sorted(x2)
#print(x2)
#
#z[0]=22
#z[1]=5
#
#x2 = [("a",3,z), ("c",1,y), ("b",5,x)]
#
##sorted(x2, key=lambda s:s[2])
##print(x2)
##print("*******************")
##sorted(x2, key=lambda s:s[2][1])
##print(x2)