# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 12:17:23 2018

@author: 612383300
"""

#print("Hello world!")
#print("Hello again!")
#print("I like typing this")
#print("This is done")
#print("Yay! Printing")
#print("I'd much rather you 'not'.")
#print('I "said" do not touch this.')


##ex3
#
#print ("I will now count my chickens:")
#
#print ("Hens", 25 + 30 / 6)
#
#print ("Roosters", 100 - 25 * 3 % 4)
#
#print ("Now I will count the eggs:")
#
#print (3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
#
#print ("Is it true that 3 + 2 < 5 - 7?")
#
#print (3 + 2 < 5 - 7)
#
#print ("What is 3 + 2?", 3 + 2)
#
#print ("What is 5 - 7?", 5 - 7)
#
#print ("Oh, that's why it's False.")
#
#print ("How about some more.")
#
#print ("Is it greater?", 5 > -2)
#
#print ("Is it greater or equal?", 5 >= -2)
#
#print ("Is it less or equal?", 5 <= -2)


##ex4
#
#cars = 100
#space_in_a_car = 4
#drivers = 30
#passengers = 90
#cars_not_driven = cars - drivers
#cars_driven = drivers
#carpool_capacity = cars_driven * space_in_a_car
#average_passengers_per_car = passengers / cars_driven
#
#
#print ("There are", cars, "cars available.")
#print ("There are only", drivers, "drivers available.")
#print ("There will be", cars_not_driven, "empty cars today.")
#print ("We can transport", carpool_capacity, "people today.")
#print ("We have", passengers, "to carpool today.")
#print ("We need to put about", average_passengers_per_car, "in each car.")

#ex5
#
#my_name = 'Maggie'
#my_age = 100 
#my_height = 165 # cm
#my_weight = 53 # kg
#my_eyes = 'Brown'
#my_teeth = 'White'
#my_hair = 'Dark brown'
#
#print ("Let's talk about {}".format(my_name))
#print ("He's {} cm tall.".format(my_height))
#print ("He's {} kg heavy.".format(my_weight))
#print ("Actually that's not too heavy.")
#print ("She's got {} eyes and {} hair.".format(my_eyes, my_hair))
#print ("Her teeth are usually {} depending on the coffee.".format(my_teeth))
#
## this line is tricky, try to get it exactly right
#print ("If I add {}, {}, and {} I get {}.".format(
#    my_age, my_height, my_weight, my_age + my_height + my_weight))
#

##ex6
#
#x = "There are {} types of people.".format(10)
#binary = "binary"
#do_not = "don't"
#y = "'Those who know {} and those who {}.'".format(binary, do_not)
#
#print (x)
#print (y)
#
#print ("I said: '{}'.".format(x))
#print ("I also said: {}.".format(y))
#
#hilarious = False
#joke_evaluation = "Isn't that joke so funny?! {}"
#
#print (joke_evaluation.format(hilarious))
#
#w = "This is the left side of... "
#e = "a string with a right side."
#
#print (w + e)

#ex6 version 2

#types_of_people = 10
#x = f"There are {types_of_people} types of people."
#
#binary = "binary"
#do_not = "don't"
#y = f"Those who know {binary} and those who {do_not}."
#
#print(x)
#print(y)
#
#print(f"I said: {x}")
#print(f"I also said: '{y}'")
#
#hilarious = False
#joke_evaluation = "Isn't that joke so funny?! {}"
#print(joke_evaluation.format(hilarious))
#
#w = "This is the left side of ..."
#e = "a string with a right side."
#
#print (w + e)


##ex7
#
#print ("Mary had a little lamb.")
#print ("Its fleece was white as {}.".format('snow'))
#print ("And everywhere that Mary went.")
#print ("." * 10)  # what'd that do?
#
#end1 = "C"
#end2 = "h"
#end3 = "e"
#end4 = "e"
#end5 = "s"
#end6 = "e"
#end7 = "B"
#end8 = "u"
#end9 = "r"
#end10 = "g"
#end11 = "e"
#end12 = "r"
#
## watch end = ' ' at the end. try removing it to see what happens.
#print (end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
#print (end7 + end8 + end9 + end10 + end11 + end12)

##ex8
#
#formatter = "{} {} {} {}"
#
#print (formatter.format(1, 2, 3, 4))
#print (formatter.format("one", "two", "three", "four"))
#print (formatter.format(True, False, False, True))
#print (formatter.format(formatter, formatter, formatter, formatter))
#print (formatter.format(
#    "I had this thing.",
#    "That you could type up right.",
#    "But it didn't sing.",
#    "So I said goodnight."
#))

##ex9
#days = "Mon Tue Wed Thu Fri Sat Sun"
#months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
#
#print("Here are the days: ", days)
#print("Here are the months: ", months)
#
#print("""
#      There's something going on here.
#      With the three double-quotes.
#      We'll be able to type as much as we like.
#      Even 4 lines if we want, or 5, or 6.
#      """)

##ex10
#
#tabby_cat = "\tI'm tabbed in."
#persian_cat = "I'm split\non a line."
#backslash_cat = "I'm \\ a \\ cat."
#
#fat_cat = """
#I'll do a list:
#    \t* Cat food
#    \t* Fishies
#    \t* Catnip\n\t* Grass
#    """
#    
#print(tabby_cat)
#print(persian_cat)
#print(backslash_cat)
#print(fat_cat)