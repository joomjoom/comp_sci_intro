# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 23:52:11 2018

@author: Jumma
"""

def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    #YOUR CODE HERE
    
    if max(a,b) % min(a, b) == 0:
        return min(a, b)
    else:
        return gcd(min(a, b), max(a, b) % min(a, b))