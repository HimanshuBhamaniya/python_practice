'''Function for creating Diomand shape with letters.'''
import string
ALPHA = string.ascii_uppercase
def rows(letter):
    '''Creates a diamond pattern using letters.
    parameter:
        letter (str): Its the given letter.
    return (list): It returns a list of lines that form daimod pattern.'''
    index = ALPHA.index(letter)
    lines = []
    for num in range(index + 1):
        if num == 0:
            row = ' ' * (index - num) + ALPHA[num] + ' ' * (index - num)
        else:
            row = ' ' * (index - num) + ALPHA[num] + ' ' * (2 * num - 1) + ALPHA[num] + ' ' * (index - num)
        lines.append(row)
    return lines + lines[-2::-1]

    
    
