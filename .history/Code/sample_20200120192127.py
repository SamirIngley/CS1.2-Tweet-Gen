from stochastic import stoch
import random

def prob_sample(histo):

    words = stoch(histo)

    dart = random.randint(0, 100)
    counter = 0
    word = None
    
    for pair in words:
        counter += pair[1]
        word = pair[0]
