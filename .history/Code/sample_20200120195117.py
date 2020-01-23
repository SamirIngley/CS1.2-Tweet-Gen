from stochastic import stoch
from histogram import list_hist
import random

def prob_sample(histo):
    ''' Input a histogram. Output a randomly chosen word from the histogram
    relative to its frequency in the body of text.  
    '''

    words = stoch(histo)
    # print(words)

    dart = random.randint(0, 100)
    counter = 0
    word = None
    
    for pair in words:
        if counter < dart:
            counter += pair[1]
            word = pair[0]

    return dart, counter, word

if __name__ == "__main__":
    listo_histo = list_hist("source.txt")
    print(prob_sample(listo_histo))