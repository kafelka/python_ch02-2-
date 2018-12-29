#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 01:29:36 2018

@author: mag
Coding bat List2
"""
#Return the number of even ints in the given array. Note: the 
#% "mod" operator computes the remainder, e.g. 5 % 2 is 1.
#count_evens([2, 1, 2, 3, 4]) → 3
#count_evens([2, 2, 0]) → 3
#count_evens([1, 3, 5]) → 0

def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count += 1          
    return count

print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))
############################
print("\n")

def count_fives(nums):
    count = 0
    for num in nums:
        if num == 5:
            count += 1
    return count

print(count_fives([1, 3, 5]))
############################
print("\n")

#Given an array length 1 or more of ints, return the difference between 
#the largest and smallest values in the array. Note: the built-in 
#min(v1, v2) and max(v1, v2) functions return the smaller or larger of 
#two values.
#big_diff([10, 3, 5, 6]) → 7
#big_diff([7, 2, 10, 9]) → 8
#big_diff([2, 10, 7, 2]) → 8

def big_diff(nums):
    return max(nums) - min(nums)

print(big_diff([10, 3, 5, 6]))
print(big_diff([7, 2, 10, 9]))
print(big_diff([2, 10, 7, 2]))
############################
print("\n")

#Return the "centered" average of an array of ints, which we'll 
#say is the mean average of the values, except ignoring the largest and 
#smallest values in the array. If there are multiple copies of the 
#smallest value, ignore just one copy, and likewise for the largest value. 
#Use int division to produce the final average. You may assume that 
#the array is length 3 or more.
#centered_average([1, 2, 3, 4, 100]) → 3
#centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
#centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(nums):
    nums.remove(max(nums))
    nums.remove(min(nums))
    return int(sum(nums) / len(nums))


print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))
############################
print("\n")



############################
print("\n")



############################
print("\n")