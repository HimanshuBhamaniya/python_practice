'''Function to find prime factors of a number.'''
def factors(value):
    '''Finds prime factors of a given number.
    parameter:
        value (int): Its the given number.
    return (list): It returns a list of prime factors of a given number.'''
    prime_factor = []
    while value % 2 == 0:
        prime_factor.append(2)
        value //= 2
    factor = 3
    while factor * factor <= value:
        while value % factor == 0:
            prime_factor.append(factor)
            value //= factor
        factor += 2
    if value > 1:
        prime_factor.append(value)
    return prime_factor
