'''This funtion converts a string of binary number into a
sequence of actions that is used to identiy club members.'''
def commands(binary_str):
    '''Converts a binary number string into a list of actions.
    parameter:
        binary_str (str): The binary number string that needs to be converted.
    
    return (list): It returns a sequence of actions that can help identify club
                   members.
    '''
    actions = ['wink', 'double blink', 'close your eyes', 'jump']
    sequence = []
    for digit, action in zip(binary_str[::-1][:4], actions):
        if digit == '1':
            sequence.append(action)
    if len(binary_str) == 5 and binary_str[0] == '1':
        sequence.reverse()
    return sequence
    
        
        
