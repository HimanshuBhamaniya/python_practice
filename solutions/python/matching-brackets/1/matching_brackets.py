'''Function for checking if all the brackets in a string is balanced or not. '''
def is_paired(input_string):
    '''Checks if brackets in a given string is balanced.
    parameter:
        input_string (str): Its the given string.
    return (bool): It return True if all brackets are balanced else False.'''
    pair = {')':'(', '}':'{', ']':'['}
    stack = []
    for item in input_string:
        if item in '({[':
            stack.append(item)
        elif item in ')}]':
            if not stack or stack[-1] != pair[item]:
                return False
            stack.pop()
    return not stack
