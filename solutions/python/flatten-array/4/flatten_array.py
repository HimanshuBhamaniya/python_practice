'''This is a function to flatten a nested list.'''
def flatten(itterable):
    '''Flattens the given nested list.
    parameter:
        itterable (list): The given list that needs to be flatten.
    return (list): It returns a flatten list.'''
    flat_list = []
    for item in itterable:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        elif item is not None:
            flat_list.append(item)
    return flat_list
    
