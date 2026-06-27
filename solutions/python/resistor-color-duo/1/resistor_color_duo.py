'''This is function that tells the numeric values of first two color band of a resistor. '''
LOOKUP = {'black': 0,
          'brown': 1,
          'red': 2,
          'orange': 3,
          'yellow': 4,
          'green': 5,
          'blue': 6,
          'violet': 7,
          'grey': 8,
          'white': 9}

def value(colors):
    '''Identifies the numeric values of first two color bands of a resistor.
    parameter:
        colors (list): The list of color bands on a resistor.
    return (int): The numeric values of first two color bands on a resistor.'''
    return int(''.join([str(LOOKUP[colors[0]]) ,str(LOOKUP[colors[1]])]))
