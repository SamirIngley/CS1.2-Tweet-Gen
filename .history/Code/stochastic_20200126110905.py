import random
from histogram import unique_words, frequency, list_hist

def stoch(histo):
    ''' Lists  list_hist
    Stochastic sampling means taking an element from a given collection at random 
    This returns a list of percentages of word frequencies in a histogram
    '''

    percentages = []

    total_wc = 0    # total word count
    for item in histo:
        total_wc += int(item[1])

    for item in histo:
        # freq = frequency(item[0], histo)
        perc = (item[1] / total_wc) * 100
        instance = (item[0], perc)
        percentages.append(instance)

    return percentages

        


if __name__ == "__main__":
    listo_histo = list_hist("source.txt")
    print(stoch(listo_histo))
