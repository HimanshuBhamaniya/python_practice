'''Function for finding date and time after one gigaseconds after a given date. '''
from datetime import timedelta
def add(moment):
    '''Calculates date and time one gigaseconds after the given date.
    parameter:
        moment (datetime): Its the given date.
    return (datetime): It returns date and time after one gigaseconds.'''
    tmdlta = timedelta(seconds= 1_000_000_000)
    return moment + tmdlta
