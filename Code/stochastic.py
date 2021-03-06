import random
from histogram import unique_words, frequency, list_hist

def stoch(histo):
    ''' Lists  list_hist
    This function returns a list of percentages of word frequencies in a histogram
    Stochastic sampling means taking an element from a given collection at random 
    '''

    percentages = []

    total_wc = 0    # total word count
    for item in histo:
        total_wc += int(item[1])

    for item in histo:
        percent = (item[1] / total_wc) * 100   # calculate percentage based on freq / total
        instance = (item[0], percent)
        percentages.append(instance)

    return percentages

        


if __name__ == "__main__":
    listo_histo = list_hist("source.txt")
    print(stoch(listo_histo))
