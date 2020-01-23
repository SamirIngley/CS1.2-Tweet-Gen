import random
from histogram import unique_words, frequency, list_hist

def stochastic(histo):
    ''' Stochastic sampling means taking an element from a given collection at random '''
    total_unique = unique_words(histo) # number of unique words
    print(unique)
    rand_num = random.randint(1, total_unique) # random number in range of number of unique words
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
    source = 'one fish two fish red fish blue fish'
    stochastic(list_hist(source))