# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 16:16:01 2018

@author: Jumma
"""

s = "asdfbobasdfbob"

count = 0
for index in range(len(s)-2):
    if s[index:index+3] == "bob":
        count += 1
print("Number of times bob occurs is: " + str(count))
