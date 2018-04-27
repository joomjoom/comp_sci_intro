# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 22:16:23 2018

@author: Jumma
"""

def polysum(n, s):
    '''
    n: int, number of sides
    s: int or float, length of sides
    
    This function returns the area plus the square of the perimeter 
    of an n sided polygon with side lengths of s.
    '''
    import math
    area =(.25 * n * s**2)/math.tan(math.pi/n)
    perim = n*s
    
    return round(area + perim**2, 4)
    