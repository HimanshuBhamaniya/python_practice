'''This is a function to determine if a word or phrase is an isogram.
'''
def is_isogram(string):
    '''Identifies if a word or phrase is an isogram (have no
       repeating letter).
    parameter:
        string (str): Its the word or phrase that have to be checked.
    return (bool): It return True if the string is an isogram.'''
    letters_list = list(ltr.lower() for ltr in string if ltr.isalpha())
    for item in letters_list:
        if not letters_list.count(item) == 1:
            return False
    return True
    
