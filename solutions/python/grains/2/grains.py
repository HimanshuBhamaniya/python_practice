def square(number:int):
    """
    calculate the amount of grain on nth square of a chessboard
    
    parameter:
      number int(): the number of the square from the chessboard to find the amount of grain on it.
    
    return: int(): the amount of grain on the nth square.
    
    """
    
    if number<1 or number >64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)
        
        


def total():
    return 2**64-1
        
