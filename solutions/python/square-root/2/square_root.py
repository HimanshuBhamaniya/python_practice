'''function for finding square root of number.'''
def square_root(number):
    '''Calculates square root of given number.
    parameter:
        number (int): The number whose square number is to be found.
    return (int): Square root of the given number.'''
    for num in range(1, number+1):
        if num*num == number:
            return num
    return None