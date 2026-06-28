'''This program will help you find the resistor\'s label by a list of color bands.'''
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
TOLERANCE = {'grey': '0.05%',
            'violet': '0.1%',
            'blue': '0.25%',
            'green': '0.5%',
            'brown': '1%',
            'red': '2%',
            'gold': '5%',
            'silver': '10%'}
def resistor_label(colors):
    '''Identifies the resistor\'s label based on the list of colors.
    parameter:
        colors (list): The list of color bands of a resistor.
    return (str): It return a string that indicates resistor\'s resistance and tolerance.
    '''
    metric_prefix = [
        (1000000000, 'gigaohms'),
        (1000000, 'megaohms'),
        (1000, 'kiloohms'),
        (1, 'ohms')
    ]
    for format, name in metric_prefix:
        if resistance(colors) == 0:
            return f'0 ohms'
        if resistance(colors) >= format:
            value = resistance(colors) / format
            return f'{value:g} {name} \u00b1{TOLERANCE[colors[4]] if len(colors) == 5 else TOLERANCE[colors[3]]}'
    return f'{resistance(colors)} ohms \u00b1{TOLERANCE[colors[4]] if len(colors) == 5 else TOLERANCE[colors[3]]}'
            
def resistance(colors):
    '''Calcutates the resistance of a resistor based on the list of color bands.
    parameter:
        colors (list): The list of color bands of a resistor.
    return (int): It returns the resistance.'''
    if len(colors) == 1:
        return 0
    if len(colors) == 5:
        return ((LOOKUP.get(colors[0], 0) * 100) + (LOOKUP.get(colors[1], 0) * 10) + LOOKUP.get(colors[2], 0)) * 10 ** LOOKUP.get(colors[3], 0)
    return ((LOOKUP.get(colors[0], 0) * 10) + LOOKUP.get(colors[1], 0)) * 10 ** LOOKUP.get(colors[2], 0)
    
