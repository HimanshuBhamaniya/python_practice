'''A Function for changing the data format and point values of letters.'''
def transform(legacy_data):
    '''Converts the data format and point values of letters based on the legacy_data.
    parameter:
        legacy_data (dict): It is the data that stores letters in groups based on their
                            score, in one to many mapping.
    return: 
        new_data (dict): It returns new_data with changed format and one to one                                  mapping.'''
    new_data = {}
    for key, item in legacy_data.items():
        for alpha in item:
            new_data[alpha.lower()] = key     
    return dict(sorted(new_data.items()))
    
