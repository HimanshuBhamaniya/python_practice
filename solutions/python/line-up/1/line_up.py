'''Function to produce a sentence using custoner's name and their number at the queue as an ordinal numeral. '''
def line_up(name, number):
    '''Generates a sentence using name and number as an ordinal numeral.
    parameter:
        name (str): Name of the customer.
        number (int): Number of the customer in deli's queue.
    return (str): A string of sentence with customer's name and number.'''
    last_two_digits = number % 100
    last_digit = number % 10
    if 10 <= last_two_digits < 20:
        suffix = 'th'
    elif last_digit == 1:
        suffix = 'st'
    elif last_digit == 2:
        suffix = 'nd'
    elif last_digit == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    
    return f'{name}, you are the {number}{suffix} customer we serve today. Thank you!'
