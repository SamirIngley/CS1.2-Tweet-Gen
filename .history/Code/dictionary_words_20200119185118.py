import random


def random_words(num):
    ''' uses words list in Unix
    takes in a number returns a sentence 
    from the word list of random order 
    with the number of words inputted
    '''
    
    wl = open('/usr/share/dict/words', 'r')
    wordlist = wl.readlines()
    wl.close()

    sentence = []

    for word in range(num):
        rand
