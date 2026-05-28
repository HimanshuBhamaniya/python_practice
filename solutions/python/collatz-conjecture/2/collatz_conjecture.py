def steps(number:int):
    """
     calculate the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture.
  
    parameter:
       number(int): The positive integer number on which Collatz Conjecture rule will be applied.

    return:
       int: numbers of steps it took to reach 1.
  
    example:
       >>> steps(12)
           9
       >>> steps(7)
           16
           """
    if number<=0:
        raise ValueError("Only positive integers are allowed")
    count=0
    while True:
        count+=1
        if number==1:
            break
        else:
            if number%2==0:
               number=number/2 
            else:
               number=(number*3)+1
    return count-1
