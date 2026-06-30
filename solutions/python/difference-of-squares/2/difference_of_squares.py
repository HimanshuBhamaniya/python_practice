'''This program is useful for finding difference between the square of 
   the sum and the sum of the squares of the first N natural numbers.'''
def square_of_sum(number):
    '''Calculates the square of sum of first N natural numbers.
    parameter:
        number (int): It is the value of N natural numbers.
    return (int): It returns the square of sum.'''
    sum_of_number = sum(num for num in range(1, number + 1))
    return sum_of_number ** 2
    
def sum_of_squares(number):
    '''Calculates the sum of squares of first N natural numbers.
    parameter:
        number (int): It is the value of N natural numbers.
    return (int): It returns the sum of squares.'''
    return sum(num ** 2 for num in range(1, number + 1))
    
def difference_of_squares(number):
    '''Calculates the difference between the square of sum and sum of squares.
    parameter:
        number (int):It is the value of N natural numbers.
    return (int): It returns the difference between square of sum and sum of squares.'''
    return square_of_sum(number) - sum_of_squares(number)