'''This is a program that encodes any text according to Atbash cipher, an ancient
encryption system created in the Middle East.'''
import string
cipher = dict(zip (string.ascii_lowercase, string.ascii_lowercase[::-1]))
def encode(plain_text):
    '''Encodes the given string according to Atbash cipher.
    parameter:
        plain_text (str): It the given string.
    return (str): It returns an encrypted string.'''
    encoded_str = ''.join(cipher.get(char, char) for char in plain_text.lower() if char.isalnum())
    chunks = [encoded_str[elem:elem+5] for elem in range(0, len(encoded_str), 5)]
    return ' '.join(chunks)

def decode(ciphered_text):
    '''Decodes the given encrypted string into tangible form.
    parameter:
        ciphered_text (str): It the given encrypted string.
    return (str): It returns a string in tangible form.'''
    return ''.join(cipher.get(char, char) for char in ciphered_text.lower() if char.isalnum())
