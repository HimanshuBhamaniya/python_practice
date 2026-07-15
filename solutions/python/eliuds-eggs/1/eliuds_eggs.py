'''Function for conveerting decimal value into binary and counting it's ones.'''
def egg_count(display_value):
    '''Calculates the count of eggs in the coop.
    parameter:
        display_value (int): Its the given decimal value.
    return (int): It returns the count of eggs in the coop.'''
    bits = []
    while display_value:
        bits.append(display_value % 2)
        display_value = display_value // 2
    return bits.count(1)
