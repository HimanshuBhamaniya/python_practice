''' This is a function that will return True is a given sentence is a pangram.
'''
def is_pangram(sentence):
    ''' Identifies if the given sentence is a pangram or not by checking
        if english_alphabets is a subset of sentence_letters.
    parameter:
        sentence (str): This is the given sentence that have to be
                        checked.
    return (bool): It returns True or False based on the .issubset()
                   results.
    '''
    sentence_letters = set()
    english_alphabets = set('abcdefghijklmnopqrstuvwxyz')
    for letter in sentence:
        letter = letter.lower()
        if letter not in sentence_letters:
            sentence_letters.add(letter)
        continue
    if english_alphabets.issubset(sentence_letters):
        return True
    return False
    
    
        
        
