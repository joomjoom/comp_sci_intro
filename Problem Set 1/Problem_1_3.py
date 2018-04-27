# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 16:29:26 2018

@author: Jumma
"""

s = "rdzqzxuwjfbzxdzdravye"
#s = "fcphcwuzkbcecaw"
alpha = 'abcdefghijklmnopqrstuvwxyz'
longest = ''
checkNext = ''

for i in range(len(s)):
    checkNext = s[i]
    print("start of loop, checkNext = " + checkNext)
    j = i
    print("i is at: " + str(i))
    print("j is at: " + str(j))
    while j+1 <= len(s)-1:
        print("entering while loop")
        if alpha.index(s[j+1]) >= alpha.index(s[j]):
            print("next letter is in order")
            checkNext = checkNext + s[j+1]
            print("checkNext is now: " + checkNext)
        else:
            break
        j += 1
        print("in the while loop j is now: " + str(j))
    if len(checkNext) > len(longest):
        longest = checkNext
        print("longest is now: " + longest)
print("Longest substring in alphabetical order is: " + longest)

        