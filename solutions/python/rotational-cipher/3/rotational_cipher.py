'''This is a function that rotate the letters acccording to key.'''
import string
ALPHABET = string.ascii_lowercase
def rotate(text, key):
    '''
    parameter:
           text (str): It is the given string.
           key (int): It is the number by which its gonna rotate.
    return (str): It returns the string with transposed letters.'''
    result = ""
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                result += ALPHABET[(ALPHABET.index(letter.lower()) + key) % 26].upper()
            else:
                result += ALPHABET[(ALPHABET.index(letter) + key) % 26]
        else:
            result += letter
    return result

