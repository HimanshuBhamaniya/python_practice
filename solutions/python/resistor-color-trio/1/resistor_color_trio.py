'''This program returns resistance in proper format based on the list of color bands. '''
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

def label(colors):
    '''Calculates the formated resistance of a resistor based on the color bands list.
    parameter: 
        colors (list): The list of color bands of a resistor.
    return (str): Properly formated resistance.'''
    main_value = LOOKUP[colors[0]] * 10 + LOOKUP[colors[1]]
    resistance = main_value * 10 ** LOOKUP[colors[2]]
    return format_resistance(resistance)

def format_resistance(ohms):
    '''Properly formates the resistance based on metric prefixes.
    parameter:
        ohms (int): The raw value of resistance.
    return (str): Formated value of resistance based on metric prefixes.'''
    prefixes = [
        (1000000000, 'gigaohms'),
        (1000000, 'megaohms'),
        (1000, 'kiloohms'),
        (1, 'ohms')
    ]
    for factor, name in prefixes:
        if ohms >= factor:
            value = ohms / factor
            return f'{value:g} {name}'
    return f'{ohms} ohms'
    
        
