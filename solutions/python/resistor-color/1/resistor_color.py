'''Functionality of this program is the provide the ability to look up value of the color band based on the ENCODING SCHEME.'''
ENCODING_SCHEME = {'black': 0,
                   'brown': 1,
                   'red': 2,
                   'orange': 3,
                   'yellow': 4,
                   'green': 5,
                   'blue': 6,
                   'violet': 7,
                   'grey': 8,
                   'white': 9}
def color_code(color):
    '''This function returns the numerical value associated with the particular color band.
    parameter:
        color (str): This the color of the band for look up.
    return (int): It returns the integer numerical values of the color band.'''
    return ENCODING_SCHEME[color]


def colors():
    '''This function returns list of different band colors.
    '''
    return list(ENCODING_SCHEME.keys())
