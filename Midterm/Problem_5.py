# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 20:59:19 2018

@author: Jumma
"""

#aDict = {1:123, 2:33, 3:5, 4:5}
#aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    def unique(aDict):
        uniqueList = []
        for key in aDict:
            count = 0
            for key2 in aDict:
                if aDict[key] == aDict[key2]:
                    count += 1
            if count < 2:
                uniqueList.append(key)
        return uniqueList
    
#    def sort(uniqueDict):
#        sortedList = []
#        while len(uniqueDict) > 0:
#            minKey = min(uniqueDict, key = uniqueDict.get)
#            sortedList.append(minKey)
#            del(uniqueDict[minKey])
#        return sortedList
    
    newList = unique(aDict)
    newList.sort()
    return newList