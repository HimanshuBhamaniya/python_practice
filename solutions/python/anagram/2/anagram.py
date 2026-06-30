'''This is useful for finding anagrams of a given word.'''
def find_anagrams(word, candidates):
    '''Identifies the anagrams of a given word from the candidates list of words.
    parameter:
        word (str): The word whose anagrams are to be found.
        candidates (list): The list of candidate words from which anagrams are to be found.
    return (list): It returns a list of valid anagrams.'''
    return [
        anagram for anagram in candidates
        if word.casefold() != anagram.casefold()
        and sorted(anagram.casefold()) == sorted(word.casefold())
    ]
