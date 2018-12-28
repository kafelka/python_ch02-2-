# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:05:35 2018

@author: nahas
"""
#CodingBat WarmUp2 exercises

#Given a string and a non-negative int n, return a larger string that is 
#n copies of the original string.
#string_times('Hi', 2) → 'HiHi'
#string_times('Hi', 3) → 'HiHiHi'
#string_times('Hi', 1) → 'Hi'

def string_times(str, n):
  return str * n

print(string_times("Hiya!", 2))

############################
print("\n")


#Given a string and a non-negative int n, we'll say that the front of the 
#string is the first 3 chars, or whatever is there if the string is less
# than length 3. Return n copies of the front;
#front_times('Chocolate', 2) → 'ChoCho'
#front_times('Chocolate', 3) → 'ChoChoCho'
#front_times('Abc', 3) → 'AbcAbcAbc'

def front_times(str, n):
    return n * str[:3]

print(front_times("Juice", 4))

############################
print("\n")

#Given a string, return a new string made of every other char starting with 
#the first, so "Hello" yields "Hlo".
#string_bits('Hello') → 'Hlo'
#string_bits('Hi') → 'H'
#string_bits('Heeololeo') → 'Hello'

def string_bits(str):
    result = ""
    for n in range(len(str)):
        if n % 2 == 0:
            result = result + str[n]
    return result

print(string_bits("Python"))

############################
print("\n")

#Given a non-empty string like "Code" return a string like "CCoCodCode".
#string_splosion('Code') → 'CCoCodCode'
#string_splosion('abc') → 'aababc'
#string_splosion('ab') → 'aab'

def string_splosion(str):
    result = ""
    for n in range(len(str)):    
        result = result + str[:n+1]
    return result

print(string_splosion("Yellow"))

############################
print("\n")


#Given a string, return the count of the number of times that a substring
#length 2 appears in the string and also as the last 2 chars of the string,
#so "hixxxhi" yields 1 (we won't count the end substring).
#last2('hixxhi') → 1
#last2('xaxxaxaxx') → 1
#last2('axxxaaxx') → 2

def last2(str):
    lastTwo = str[-2:]
    firstPart = str[:-2]
    
    count = 0
    for n in range(len(firstPart)):
        if firstPart[n:n+2] == lastTwo:
            count += 1
            
    return count
    
print(last2("Blur"))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))
print(last2("xxxx"))

############################
print("\n")


#Given an array of ints, return the number of 9's in the array.
#array_count9([1, 2, 9]) → 1
#array_count9([1, 9, 9]) → 2
#array_count9([1, 9, 9, 3, 9]) → 3

def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count = count + 1
    return count

print(array_count9([1,2,9]))
print(array_count9([9,9,9]))
print(array_count9([9,9,9,9]))
print(array_count9([1,2,4]))

############################
print("front9 \n")

#Given an array of ints, return True if one of the first 4 elements in 
#the array is a 9. The array length may be less than 4.
#array_front9([1, 2, 9, 3, 4]) → True
#array_front9([1, 2, 3, 4, 9]) → False
#array_front9([1, 2, 3, 4, 5]) → False

def array_front9(nums):
    first4 = nums[:4]

    for i in range(len(first4)):
        if first4[i] == 9:
            return True
    return False


print(array_front9([1,2,9]))
print(array_front9([9,9,9]))
print(array_front9([9,9,9,9]))
print(array_front9([1,2,4]))
print(array_front9([1,2,3,4,5]))
print(array_front9([1,2,3,4,9]))

############################
print("\n")


#Given an array of ints, return True if the sequence of numbers 1, 2, 3 
#appears in the array somewhere.
#array123([1, 1, 2, 3, 1]) → True
#array123([1, 1, 2, 4, 1]) → False
#array123([1, 1, 2, 1, 2, 3]) → True

def array123(nums):
#    if 1 in nums:
#        if 2 in nums:
#            if 3 in nums:
#               return True 
#    
#    return False
    
    arr123 = set([1, 2, 3])
    
    for i in nums:
        if i in arr123:
            arr123.remove(i)
            
    return arr123 == set([])
    
print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))
############################
print("\n")


#Given 2 strings, a and b, return the number of the positions where they 
#contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, 
#since the "xx", "aa", and "az" substrings appear in the same place in both strings.
#string_match('xxcaazz', 'xxbaaz') → 3
#string_match('abc', 'abc') → 2
#string_match('abc', 'axc') → 0

def string_match(a, b):
    return


string_match('xxcaazz', 'xxbaaz') 
string_match('abc', 'abc') 
string_match('abc', 'axc') 
############################
print("\n")

def consecutive123(nums):
    
    for i in range(len(nums)-2):
        if nums[i] == 1:
            if nums[i+1] == 2:
                if nums[i+2] == 3:
                    return True
                
    return False            

print(consecutive123([1, 1, 2, 3, 1]))
print(consecutive123([1, 1, 2, 4, 1]))
print(consecutive123([1, 1, 2, 1, 2, 3]))
print(consecutive123([1, 1, 2, 4, 3]))