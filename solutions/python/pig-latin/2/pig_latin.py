''' This is a function to convert text from English to Pig Latin. 
'''
def translate(text):
    '''This function will convert text from English to Pig Latin.
    parameter 
        text (str): The text that has to be converted into Pig Latin.
    return (str): The converted text is returned.
    '''
    VOWELS_OTHER = ('xr','yt','a','e','i','o','u')
    pig_latin = []
    
    for word in text.split():
        if word.startswith(VOWELS_OTHER):
            pig_latin.append(word + 'ay')
            continue
        if 'qu' in word:
            idx = word.find('qu')
            if idx == 0:
                pig_latin.append(word[2:] + 'quay')
                continue
            elif idx > 0 and word[idx-1] not in VOWELS_OTHER:
                pig_latin.append(word[idx+2:] + word[:idx+2] + 'ay')
                continue
        if 'y' in word:
            idx = word.find('y')
            if idx != 0 and all(ch not in VOWELS_OTHER for ch in word[:idx]):
                pig_latin.append(word[idx:] + word[:idx] + 'ay')
                continue
        prefix_consonant = ''
        while len(word) > 0 and not word.startswith(VOWELS_OTHER):
            prefix_consonant += word[0]
            word = word[1:]
        if prefix_consonant:
            pig_latin.append(word + prefix_consonant + 'ay')
            continue
        
    return ' '.join(pig_latin)
        
