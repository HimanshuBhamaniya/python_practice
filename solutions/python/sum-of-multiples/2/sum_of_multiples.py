'''Function for finding the sum of multiples.'''
def sum_of_multiples(limit, multiples):
    '''Calculates the sum of multiple.
    parameter:
        limit (int): Its the range.
        multiples (list): Its the list of base values for multiples.
    return (int): It returns the sum of multiples.'''
    return sum({
        multiple
        for multiple in range(1,limit)
        for base_value in multiples
        if base_value > 0 and multiple % base_value == 0
    })
