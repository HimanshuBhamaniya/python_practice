'''Function to produce a sentence using custoner's name and their number at the queue as an ordinal numeral. '''
def line_up(name, number):
    '''Generates a sentence using name and number as an ordinal numeral.
    parameter:
        name (str): Name of the customer.
        number (int): Number of the customer in deli's queue.
    return (str): A string of sentence with customer's name and number.'''
    suffix = 'th' if number % 100 in (11,12,13) else {1:'st', 2:'nd', 3:'rd'}.get(number % 10, 'th')
    return f'{name}, you are the {number}{suffix} customer we serve today. Thank you!'
