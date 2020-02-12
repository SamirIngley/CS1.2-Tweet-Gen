from stochastic import stoch
from histogram import list_hist
import random

def prob_sample(histo):
    ''' Input a histogram. Output a randomly chosen word from the histogram
    relative to its frequency.  
    '''

    words = stoch(histo)
    # print(words)

    dart = random.randint(0, 100)
    counter = 0

    print(words)
    print(dart)
    
    
    for pair in words:   # pair = word, freq in percent
        
        print(counter)       
        print(pair)
        counter += pair[1]  # since words already in percent - we just keep adding til we hit the dart
        word = pair[0]
        if counter >= dart:
            return word
    

if __name__ == "__main__" :
    listo_histo = list_hist("source.txt")
    # dicto_histo = dict_hist("source.txt")
    # print(dicto_histo)
    print(prob_sample(listo_histo))
    # print(prob_sample(dicto_histo))