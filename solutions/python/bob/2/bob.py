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
    if hey_bob_c[len(hey_bob_c)-1] == '?' and not hey_bob_c.isupper():
        return 'Sure.'
    if hey_bob_c.isupper() and hey_bob_c[len(hey_bob_c)-1] != '?':
        return 'Whoa, chill out!'
    if hey_bob_c[len(hey_bob_c)-1] == '?' and hey_bob_c.isupper():
        return 'Calm down, I know what I\'m doing!'
    return 'Whatever.'
    
