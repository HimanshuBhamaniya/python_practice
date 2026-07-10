"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
EQUAL = 1
SUPERLIST = 2
SUBLIST = 3
UNEQUAL = 4    

def sublist(listOne, listTwo):
    '''Categorize lists into EQUAL, SUPERLIST, SUBLIST, UNEQUAL based on their properties.
    parameter:
        listOne (list): Its the first list.
        listTwo (list): Its the second list.
    return (int): It return the Enumerated constant .'''
    if listOne == listTwo:
        return EQUAL
    if all(item in listOne for item in listTwo) and is_sublist(listOne, listTwo):
        return SUPERLIST
    if all(item in listTwo for item in listOne) and is_sublist(listOne, listTwo):
        return SUBLIST
    return UNEQUAL

def is_sublist(listOne, listTwo):
    '''Checks if the given lists are sublist or not.
    parameter:
         listOne (list): Its the first list.
         listTwo (list): Its the second list.
    return (bool): It returns True if lists are sublist else return False.'''
    if len(listOne) > len(listTwo):
        for item in range(len(listOne)):
            if listOne[item:item+len(listTwo)] == listTwo:
                return True
    if len(listTwo) > len(listOne):
        for item in range(len(listTwo)):
            if listTwo[item:item+len(listOne)] == listOne:
                return True
    return False
