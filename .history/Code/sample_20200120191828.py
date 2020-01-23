from stochastic import stoch
import random

def prob_sample(histo):

    words = stoch(histo)

    dart = random.randint(0, 100)