import sample
import random
from clean_text import clean
from dictogram import Dictogram

class Markov():
    def __init__(self, corpus):
        self.corpus = clean(corpus)
        self.states = {}
        self.chain()
    
    def chain(self):


        last_word = None

        for word in self.corpus:
            if last_word is not None: # set last word line 14

                if last_word not in self.states: # if we haven't seen this word before
                    self.states[last_word] = Dictogram() # empty histogram as value
                self.states[last_word].add_count(word) # add word to last word histogram

            last_word = word # set word as last_word
        

             
    def __str__(self):
        return str(self.states)


    def random_walk():
        
        words = (self.states)
        length = len(words)
        

        rand = random.randint(0, length)

        word = (list(words)[rand])

        print(rand)
        print(words)

        # counter = 0
        # while counter < num_words:
        #     last_word = None

        #     # if this is the first word
        #     if last_word == None:   
        #         # pick a random word
        #         word = (list(words)[rand])


        
        return 




if __name__ == '__main__':
    source = 'one fish two fish red fish blue fish'
    markov = Markov('source.txt')
    # print(markov.states)
    print(markov.random_walk())

