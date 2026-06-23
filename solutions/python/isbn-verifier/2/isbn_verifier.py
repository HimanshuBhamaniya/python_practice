'''This is a function to check if the given string is a valid ISBN-10. 
'''
import re
def is_valid(isbn):
    '''Identifies if the given string is a valid ISBN-10 based on certain conditions.
    parameter:
        isbn (str): It the given string.
    return (bool): It returns True or False.
    '''
    pattern = re.compile(r'^\d-?\d{3}-?\d{5}-?[\dX]$')
    match = pattern.fullmatch(isbn)
    if not match:
        return False
    isbn_list = [chracter for chracter in isbn if chracter.isdigit() or chracter == 'X']
    result = []
    for index, element in enumerate(isbn_list):
        if element == 'X':
            value = 10
        else:
            value = int(element)
        result.append(value * (10 - index))
    return sum(result) % 11 == 0
