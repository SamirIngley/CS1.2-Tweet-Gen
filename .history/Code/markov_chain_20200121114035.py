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


    def random_walk(self, num_words=11):
        
        # length = len(self.states)
        # rand = random.randint(0, length)

        counter = 0
        last_word = None
        word = None
         
        if last_word not None:
            pickings = self.states[last_word] # dictionary of words to pick from based on last_word's hist
            total_wc = 0 # number of words in dictionary for a word
            dart = random.int(0, 100)
            counter = 0

            for value in pickings.values(): # calculates total word count
                total_wc += value
            
            for key,value in pickings.items():
                while counter < dart
                    counter += value / total_wc
                    last_word = key
            

        word = (list(self.states)[rand])

        current_word = self.states[last_word]
        print(current_word)

        for word in self.states.keys():





        # while counter < num_words:

        #     # if this is not the first word
        #     if last_word:   
        #         word_hist = self.states[last_word]
        #         wor_hist.

        #     else:
        #         # pick a random word
        #         word = (list(self.states)[rand])
        #         # print(word)
        #         last_word = word
                

if __name__ == '__main__':
    source = 'one fish two fish red fish blue fish'
    markov = Markov('source.txt')
    # print(markov.states)
    print(markov.random_walk())

