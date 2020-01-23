import random
from histogram import unique_words, frequency, list_hist

def stoch(histo):
    ''' Stochastic sampling means taking an element from a given collection at random '''

    percentages = []

    total_wc = 0
    for item in histo:
        if type(item[0]) == int: 
            total_wc += int(item[1])

    for item in histo:
        freq = frequency(item[0], histo)
        perc = (freq / total_wc) * 100
        instance = (item[0], perc)
        percentages.append(instance)
    
    return percentages


if __name__ == "__main__":
    listo_histo = list_hist("source.txt")
    print(stoch(listo_histo))
