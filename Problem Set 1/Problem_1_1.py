# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 16:06:55 2018

@author: Jumma
"""

s = "hello world"
count = 0
for letter in s:
    if letter == "a" or letter == "e" or letter == "i" \
    or letter == "o" or letter == "u":
        count += 1

print("Number of vowels: " + str(count))