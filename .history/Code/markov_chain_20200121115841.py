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

        sentence = []

        length = len(self.states)
        rand = random.randint(0, length)

        words_counter = 0
        last_word = None

        while num_words > words_counter:            

            if last_word:
                pickings = self.states[last_word] # dictionary of words to pick from based on last_word's hist
                print(pickings)
                total_wc = 0 # number of words in dictionary for a word
                print(total_wc)
                dart = random.randint(0, 100) # as percentage
                print(dart)

                for value in pickings.values(): # calculates total word count
                    total_wc += value
                    print(value)

                counter = 0
                for key,value in pickings.items():
                    print(key, value)
                    while counter < dart:
                        counter += (value / total_wc) * 100 # as percentage
                        print(counter)
                        last_word = key
                        print(last_word)
            else:
                last_word = (list(self.states)[rand])

            sentence.append(last_word)

        return sentence


if __name__ == '__main__':
    source = 'one fish two fish red fish blue fish'
    markov = Markov('source.txt')
    print(markov.states)
    print('')
    print(markov.random_walk())

