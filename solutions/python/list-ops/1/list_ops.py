'''In this program we have implemented basic list operations'''
def append(list1, list2):
    return list1 + list2

def concat(lists):
    result = []
    for lst in lists:
        result.extend(lst)
    return result

def filter(function, list):
    filtered_list = []
    for item in list:
        if function(item):
            filtered_list.append(item)
    return filtered_list

def length(list):
    count = 0
    for item in list:
        count += 1
    return count
        
def map(function, list):
    result = []
    for item in list:
        result.append(function(item))
    return result

def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial

def foldr(function, list, initial):
    for item in list[::-1]:
        initial = function(initial, item)
    return initial

def reverse(list):
    return list[::-1]