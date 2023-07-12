"""
Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4]
"""

import collections

def capital_indexes(val):
    capitals = []

    return capitals



def arrays_match(a1, a2):
    if collections.Counter(a1) == collections.Counter(a2):
        print ("Success")
    else:
        print ("Fail - result does not match")


arrays_match(capital_indexes(""), [])
arrays_match(capital_indexes("AbCdeF"), [0,2,5])
arrays_match(capital_indexes("only One capital"), [5])
arrays_match(capital_indexes("HELLO"), [0,1,2,3,4])
arrays_match(capital_indexes("there are no capitals here"), [])
arrays_match(capital_indexes("This 0ne H@s $ym_bolS"), [0,9,20])
arrays_match(capital_indexes(None), [])
