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
    if all(item in list_one for item in list_two) and is_sublist(list_one, list_two):
        return SUPERLIST
    if all(item in list_two for item in list_one) and is_sublist(list_one, list_two):
        return SUBLIST
    return UNEQUAL

def is_sublist(list_one, list_two):
    '''Checks if the given lists are sublist or not.
    parameter:
         list_one (list): Its the first list.
         list_two (list): Its the second list.
    return (bool): It returns True if lists are sublist else return False.'''
    if len(list_one) > len(list_two):
        for item in range(len(list_one)):
            if list_one[item:item+len(list_two)] == list_two:
                return True
    if len(list_two) > len(list_one):
        for item in range(len(list_two)):
            if list_two[item:item+len(list_one)] == list_one:
                return True
    return False
