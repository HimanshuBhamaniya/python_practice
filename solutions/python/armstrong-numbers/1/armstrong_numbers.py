def is_armstrong_number(number: str):
    """ Determine whether a number is an Armstrong number.
    parameter:
        number(str): The number you want to check if its Armstrong or not.
    return: 
        (bool): It returns True if the number is Armstrong else False.
    """
    number=str(number)
    num_list= list(number) 
    pow_num_list= [int(item)**len(num_list) for item in num_list ]
    return sum(pow_num_list) == int(number)
