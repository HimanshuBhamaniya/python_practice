''' This is a function that will return True is a given sentence is a pangram.
'''
def is_pangram(sentence):
    ''' Identifies if the given sentence is a pangram or not by checking
        if english_alphabets is a subset of sentence_lowercase.
    parameter:
        sentence (str): This is the given sentence that have to be
                        checked.
    return (bool): It returns True or False based on the .issubset()
                   results.
    '''
    english_alphabets = set('abcdefghijklmnopqrstuvwxyz')
    sentence_lowercase = sentence.lower()
    return english_alphabets.issubset(sentence_lowercase)

    
    
        
        
