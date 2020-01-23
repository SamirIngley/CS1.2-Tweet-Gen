from stochastic import stoch
from histogram import list_hist
import random

def prob_sample(histo):

    words = stoch(histo)

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