# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 17:16:18 2018

@author: 612383300
"""
#CodinfBat String 1 exercises

def make_out_word(out, word):
#    return "{}{}{}".format(out[0:2], word, out[2:4])
#    return "{}{}{}".format(out[:2], word, out[2:])
#    return "{}{}{}".format(out[0]+out[1], word, out[2]+out[3])
    return "{}{}{}".format(out[:2], word, out[-2:])
    
print(make_out_word("<<>>", "Wassuuuup"))

print("#######################################################")
def first_half(str):
    x = str[0:len(str)//2]
    y = str[len(str)//2:]
    return x + "\n" + y
    
print(first_half("mojanoga"))

print("#######################################################")
def make_abba(a, b):
  return "{}{}{}{}".format(a,b,b,a)

print(make_abba("plup", "plip"))

print("#######################################################")
def make_tags(tag, word):
#    return "{}{}{}".format("<" + tag + ">", word, "</" + tag + ">")
#    return f"<{tag}>{word}</{tag}>"
    return "<{t}>{w}</{t}>".format(t=tag, w=word)


print(make_tags("div", "division"))

print("#######################################################")
def extra_end(str):
#    return ("{}".format(str[-2:]))*3
    return str[-2:]*3

print (extra_end("Zero"))

print("#######################################################")
#Given a string, return the string made of its first two chars, 
#so the String "Hello" yields "He". If the string is shorter than length 2,
# return whatever there is, so "X" yields "X", and the empty string "" yields
# the empty string "".
#first_two('Hello') → 'He'
#first_two('abcdefg') → 'ab'
#first_two('ab') → 'ab'

def first_two(str):
    return str[:2]
#    if len(str) >= 2:
#        return str[:2]
#    else:
#        return str
        
print (first_two(""))

print("#######################################################")
#Given a string, return a version without the first and last char, 
#so "Hello" yields "ell". The string length will be at least 2.
#without_end('Hello') → 'ell'
#without_end('java') → 'av'
#without_end('coding') → 'odin'

def without_end(str):
    return str[1:-1]

print(without_end("ryba"))

print("#######################################################")
#Given 2 strings, a and b, return a string of the form short+long+short,
# with the shorter string on the outside and the longer string on the inside.
# The strings will not be the same length, but they may be empty (length 0).
#combo_string('Hello', 'hi') → 'hiHellohi'
#combo_string('hi', 'Hello') → 'hiHellohi'
#combo_string('aaa', 'b') → 'baaab'

def combo_string(a, b):
    if len(a) > len(b):
        return f"{b}{a}{b}"
    else:
        return f"{a}{b}{a}"

print(combo_string("kartofel", "trefl"))

print("#######################################################")
#Given 2 strings, return their concatenation, except omit the first char
# of each. The strings will be at least length 1.
#non_start('Hello', 'There') → 'ellohere'
#non_start('java', 'code') → 'avaode'
#non_start('shotl', 'java') → 'hotlava'
def non_start(a, b):
    return a[1:] + b[1:]

print(non_start("Good", "evening"))
      
print("#######################################################")
#Given a string, return a "rotated left 2" version where the first 2 chars
# are moved to the end. The string length will be at least 2.
#left2('Hello') → 'lloHe'
#left2('java') → 'vaja'
#left2('Hi') → 'Hi'
def left2(str):
    return str[2:] + str[:2]

print (left2("evening"))