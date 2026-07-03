'''This is a function to flatten a nested list.'''
def flatten(itterable):
    '''Flattens the given nested list.
    parameter:
        itterable (list): The given list that needs to be flatten.
    return (list): It returns a flatten list.'''
    flat_list = []
    for item in itterable:
        if item == None:
            continue
        if type(item) == list:
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list
    
