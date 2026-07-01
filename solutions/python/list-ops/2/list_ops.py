'''In this program we have implemented basic list operations'''
def append(list1, list2):
    '''given two lists, add all items in the second list to the end of the first list'''
    return list1 + list2

def concat(lists):
    '''given a series of lists, combine all items in all lists into one flattened list'''
    result = []
    for lst in lists:
        result.extend(lst)
    return result

def filter(function, itterable):
    '''given a predicate and a list, return the list of all items for which predicate(item) is True'''
    filtered_list = []
    for item in itterable:
        if function(item):
            filtered_list.append(item)
    return filtered_list

def length(itterable):
    '''given a list, return the total number of items within it'''
    count = 0
    for item in itterable:
        count += 1
    return count
        
def map(function, itterable):
    '''given a function and a list, return the list of the results of applying function(item) on all items'''
    result = []
    for item in itterable:
        result.append(function(item))
    return result

def foldl(function, itterable, initial):
    '''given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator from the left'''
    for item in itterable:
        initial = function(initial, item)
    return initial

def foldr(function, itterable, initial):
    '''given a function, a list, and an initial accumulator, fold (reduce) each item into the accumulator from the right'''
    for item in itterable[::-1]:
        initial = function(initial, item)
    return initial

def reverse(itterable):
    '''given a list, return a list with all the original items, but in reversed order'''
    return itterable[::-1]