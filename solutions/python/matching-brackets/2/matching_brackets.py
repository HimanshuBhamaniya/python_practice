'''Function for checking if all the brackets in a string is balanced or not. '''
def is_paired(input_string):
    '''Checks if brackets in a given string is balanced.
    parameter:
        input_string (str): Its the given string.
    return (bool): It return True if all brackets are balanced else False.'''
    text = "".join(item for item in input_string if item in "()[]{}")
    while "()" in text or "[]" in text or "{}" in text:
        text = text.replace("()","").replace("[]", "").replace("{}","")
    return not text
