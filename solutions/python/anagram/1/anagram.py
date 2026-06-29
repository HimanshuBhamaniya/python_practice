'''This is useful for finding anagrams of a given word.'''
def find_anagrams(word, candidates):
    '''Identifies the anagrams of a given word from the candidates list of words.
    parameter:
        word (str): The word whose anagrams are to be found.
        candidates (list): The list of candidate words from which anagrams are to be found.
    return (list): It returns a list of valid anagrams.'''
    anagrams = []
    for item in candidates:
        if word.lower() == item.lower():
            continue
        if sorted(item.lower()) == sorted(word.lower()):
            anagrams.append(item)
    return anagrams
