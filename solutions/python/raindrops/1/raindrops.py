''' It is a function that turns numbers into raindrop sounds.
'''
def convert(number):
    ''' This function converts number that are divisible by 3,5,7 into its
    corresponding raindrop sounds.
    parameter: 
        number (int): The number that is to be converted into the raindrop sounds.
    return: 
        result (str): The sounds of raindrops.
    '''
    result = ''
    if number%3 == 0:
        result += 'Pling'
    if number%5 == 0:
        result += 'Plang'
    if number%7 == 0:
        result += 'Plong'
    return result if result else str(number)
    
        
