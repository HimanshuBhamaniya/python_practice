""" Its a function to find whether given year is a leap year or not.
"""

def leap_year(year):
    """ Find if current year is a leap year or not.
    parameter:
        year (int): This is the year that you want to konw 
                    if its leap year or not.
    return: 
        (bool): Return True if its leap year else False.
        
    """
    if year % 4 == 0 and (year % 100 !=0 or year % 400 == 0):
        return True
    return False
