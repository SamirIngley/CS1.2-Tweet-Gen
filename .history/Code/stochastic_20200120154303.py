import random
from histogram import unique_words, frequency, list_hist

def stoch(histo):
    ''' Stochastic sampling means taking an element from a given collection at random '''

    percentages = []

    total_wc = 0
    for item in histo:
        total_wc += int(item[1])

    for item in histo:
        freq = frequency(item[0], histo)
        perc = freq / total_wc
        instance = (item[0], perc)
        percentages.append(instance)
    
    return percentages

def stoch_sample(histo):

    percentages = stoch(histo)
    



if __name__ == "__main__":
    listo_histo = list_hist("source.txt")
    print(stoch(listo_histo))
    print(stoch_sample(listo_histo))
