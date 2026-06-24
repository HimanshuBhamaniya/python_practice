'''This is a function that rotate the letters acccording to key.'''
import string
def rotate(text, key):
    '''
    parameter:
           text (str): It is the given string.
           key (int): It is the number by which its gonna rotate.
    return (str): It returns the string with transposed letters.'''
    capital_letters = list(string.ascii_uppercase)
    lower_letters = list(string.ascii_lowercase)
    numbers = list(string.digits)
    special_characters = [' ','!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+',\
                        ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@',\
                        '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    new_text = []
    for char in text:
        if char in special_characters:
            new_text.append(char)
            continue
        if char in numbers:
            new_text.append(char)
            continue
        if char in lower_letters:
            if lower_letters.index(char)+key > 25:
                new_text.append(lower_letters[(lower_letters.index(char)+key)-26])
            else:
                new_text.append(lower_letters[(lower_letters.index(char)+key)])
        if char in capital_letters:
            if capital_letters.index(char)+key > 25:
                new_text.append(capital_letters[(capital_letters.index(char)+key)-26])
            else:
                new_text.append(capital_letters[(capital_letters.index(char)+key)])

    return ''.join(new_text)
