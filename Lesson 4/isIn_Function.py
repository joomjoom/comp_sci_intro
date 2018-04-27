# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 21:51:06 2018

@author: Jumma
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    ## I don't understand why the new search is aStr shouldn't
    ## be flipped for the recurrsion
    mid = len(aStr)//2
    if len(aStr) <= 1:
        return char == aStr
    else:
        if char > aStr[mid]:
            return isIn(char, aStr[mid+1:])
        elif char < aStr[mid]:
            return isIn(char, aStr[0:mid])
        else:
            return True