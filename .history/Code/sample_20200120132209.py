import random
from histogram import unique_words, list_histogram

def stochastic(histo):
    ''' Stochastic sampling means taking an element from a given collection at random '''
    unique = unique_words(histo) # number of unique words
    rand_num = random.randint(1, unique) # random number in range of number of unique words

    counter = 0
    word = None
    while counter < rand_num: # count until we hit the random number
        for item in histo: 
            counter += 1
            word = item
    print(word[1])
    return word[1]

if __name__ == '__main__':
    source = 'one fish two fish red fish blue fish'
    stochastic(list_histogram(source))