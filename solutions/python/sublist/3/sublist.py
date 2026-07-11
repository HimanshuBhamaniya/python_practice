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

def sublist(list_one, list_two):
    '''Categorize lists into EQUAL, SUPERLIST, SUBLIST, UNEQUAL based on their properties.
    parameter:
        list_one (list): Its the first list.
        list_two (list): Its the second list.
    return (int): It return the Enumerated constant .'''
    if list_one == list_two:
        return EQUAL
    if len(list_one) > len(list_two) and is_sublist(list_one, list_two):
        return SUPERLIST
    if len(list_one) < len(list_two) and is_sublist(list_two, list_one):
        return SUBLIST
    return UNEQUAL

def is_sublist(larger, smaller):
    '''Checks if the given lists are sublist or not.
    parameter:
         list_one (list): Its the first list.
         list_two (list): Its the second list.
    return (bool): It returns True if lists are sublist else return False.'''
    for item in range(len(larger)):
        if larger[item:item+len(smaller)] == smaller:
            return True
    return False
