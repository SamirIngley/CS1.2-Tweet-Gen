import random
import sample
from histogram import unique_words, list_hist

def stochastic(histo):
    ''' Stochastic sampling means taking an element from a given collection at random '''
    unique = unique_words(histo) # number of unique words
    print(unique)
    rand_num = random.randint(1, unique) # random number in range of number of unique words
    print(rand_num)

    counter = 0
    word = None
     # count until we hit the random number
    for item in histo:
        if counter < rand_num:
            counter += 1
            word = item

    print(word[0])
    return word[0]

if __name__ == '__main__':
    
    stochastic(list_hist('sample.txt'))