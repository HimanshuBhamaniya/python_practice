'''Function for converting a phrase into its acronym.'''
import re
def abbreviate(phrase):
    '''Converts a phrase into its acronym.
    parameter:
        phrase (str): Its the given phrase.
    return (str): It returns the acronym.'''
    phrase = phrase.replace('-',' ')
    words = re.sub(r'[!"#$%&\'\(\)*+,./:;<=>?@[\]^_`{|}~]','', phrase).split()
    return ''.join([fstl[0].upper() for fstl in words])