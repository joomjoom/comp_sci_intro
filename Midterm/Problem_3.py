# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 23:15:40 2018

@author: Jumma
"""

def count7(N, count=0):
    '''
    N: a non-negative integer
    '''
    # Your code here
    
    lastValue = N%10
    if lastValue == 7:
        count += 1
    if N // 10 == 0:
        return count
    else:
        return count7(N // 10, count)
        
        