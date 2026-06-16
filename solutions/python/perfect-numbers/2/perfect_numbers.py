""" This is a function that classify number into perfect, abundant, or deficient based on Nicomachus' (60 - 120 CE) classification scheme for positive integers.
"""
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    sum_of_factors = sum(factorization(number))
    if number <= 0:
        raise ValueError('Classification is only possible for positive integers.')
    if sum_of_factors == number:
        return 'perfect'
    if sum_of_factors < number:
        return 'deficient'
    if sum_of_factors > number:
        return 'abundant'
    

def factorization(number):
    """ Returns a list of the factors of the input integer.
    """
    factors = []
    for digit in range(1, number + 1):
        if number % digit == 0:
            if number == digit:
                break
            factors.append(digit)
    return factors

