# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 20:51:16 2018

@author: Jumma
"""
aList = ["apple", "cat", "dog", "banana"]
def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    returnList = []
    for word in aList:
        if len(word) < 4:
            returnList.append(word)
    return returnList