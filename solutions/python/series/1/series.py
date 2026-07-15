'''Function for returning all the contiguous substrings of length n in a given string in the order they appear.'''
def slices(series, length):
    '''Returns a list of contiguous substrings of length n in a given string in the order they appear.
    parameter:
        series (str): Its the given string.
        length (int): Its the length of slice.
    return (list): It returns a list of all the substrings.'''
    if len(series) == 0:
        raise ValueError('series cannot be empty')
    if length == 0:
        raise ValueError('slice length cannot be zero')
    if length < 0:
        raise ValueError('slice length cannot be negative')
    if length > len(series):
        raise ValueError('slice length cannot be greater than series length')
    return [
        series[elm:elm+length]
        for elm in range(len(series) - length + 1)
    ]