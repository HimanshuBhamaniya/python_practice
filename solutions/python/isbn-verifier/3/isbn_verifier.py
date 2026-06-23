'''This is a function to check if the given string is a valid ISBN-10. 
'''
def is_valid(isbn):
    '''Identifies if the given string is a valid ISBN-10 based on certain conditions.
    parameter:
        isbn (str): It the given string.
    return (bool): It returns True or False.
    '''
    nums = list(isbn.replace('-',''))
    if len(nums) != 10:
        return False
    if nums[-1] == 'X':
        nums[-1] = '10'
    if not all(chracter.isdigit() for chracter in nums):
        return False
    return sum(int(x) * y for x,y in zip(nums, range(10,0,-1))) % 11 == 0
