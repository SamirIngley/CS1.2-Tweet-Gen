import random
import histogram

def stochastic(histo):
    ''' Stochastic sampling means taking an element from a given collection at random '''
    unique = histogram.unique_words(histo)
    rand_num = random.randint(1, unique)

    counter = 0
    while counter < rand_num:
        for item in histo: 
            counter += 1
