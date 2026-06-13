''' This is a function that returns reply as how Bob would.
'''
def response(hey_bob):
    '''This function will reply to questions or statement as how Bob would reply to them.
    parameter (str): The statement or question asked to Bob.
    return (str): The reply to the statement or question asked to Bob.
    '''
    hey_bob_c = hey_bob.strip()
    if hey_bob_c == '':
        return 'Fine. Be that way!'
    if hey_bob_c.endswith('?') and not hey_bob_c.isupper():
        return 'Sure.'
    if hey_bob_c.endswith('?') and hey_bob_c.isupper():
        return 'Calm down, I know what I\'m doing!'
    if hey_bob_c.isupper():
        return 'Whoa, chill out!'
    return 'Whatever.'
    
