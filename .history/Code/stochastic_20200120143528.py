import random
from histogram import unique_words, frequency, list_hist

def stochastic(histo):
    ''' Stochastic sampling means taking an element from a given collection at random '''

    percentages = []

    total_wc = 0
    for item in histo:
        total_wc += int(item[1])

    for item in histo:
        freq = frequency(item[0], histo)
        perc = freq / total_wc
        instance = [item[0], perc]
        percentages.append(instance)
    
    return percentages

if __name__ == "__main__":
    source = 'one fish two fish red fish blue fish'
    stochastic(list_hist(source))
    # stochastic(list_hist(source))