'''This funtion converts a string of binary number into a
sequence of actions that is used to identiy club members.'''
def commands(binary_str):
    '''Converts a binary number string into a list of actions.
    parameter:
        binary_str (str): The binary number string that needs to be converted.
    
    return (list): It returns a sequence of actions that can help identify club
                   members.
    '''
    sequence = []
    if binary_str[4] == '1':
        sequence.append('wink')
    if binary_str[3] == '1':
        sequence.append('double blink')
    if binary_str[2] == '1':
        sequence.append('close your eyes')
    if binary_str[1] == '1':
        sequence.append('jump')
    if binary_str[0] == '1':
        sequence.reverse()
    return sequence
        
        
