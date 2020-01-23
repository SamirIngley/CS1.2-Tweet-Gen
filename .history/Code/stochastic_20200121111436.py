import random
from histogram import unique_words, frequency, list_hist, dict_hist

def stoch(histo):
    ''' Stochastic sampling means taking an element from a given collection at random 
    This returns a list of percentages of words in a histogram
    '''

    percentages = []

    total_wc = 0
    for item in histo:
        if type(item[0]) == int:
            total_wc += int(item[0])
        else:
            total_wc += int(item[1])

    for item in histo:
        if type(item[0]) == int: 
            freq = frequency(item[1], histo)
            perc = (freq / total_wc) * 100
            instance = (item[1], perc)
            percentages.append(instance)
        else:
            freq = frequency(item[0], histo)
            perc = (freq / total_wc) * 100
            instance = (item[0], perc)
            percentages.append(instance)

    return percentages


if __name__ == "__main__":
    listo_histo = list_hist("source.txt")
    dicto_histo = dict_hist("source.txt")
    print(stoch(dicto_histo))
    print(stoch(listo_histo))
