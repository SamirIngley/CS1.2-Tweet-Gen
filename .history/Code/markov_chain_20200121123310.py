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
        
        sentence = []

        sent_length = len(sentence)
        length = len(self.states)

        words_counter = 0
        last_word = None
        add_words = True

        while add_words:            

            if last_word:
                pickings = self.states[last_word] # dictionary of words to pick from based on last_word's hist
                print(pickings)
                total_wc = 0 # number of words in dictionary for last word
                print(total_wc)

                for value in pickings.values(): # calculates total word count
                    total_wc += value
                    print(value)

                dart = random.randint(0, 100) # dart as percentage
                print(dart)
                counter = 0
                for key,value in pickings.items():  # number of times each word appears
                    print(key, value)
                    while counter < dart: # when we cross the dart, we've passed the value, so the key stored is the winner
                        counter += (value / total_wc) * 100 # add number of times each word appears til we hit the dart
                        print(counter)
                        last_word = key # set last_word to the key
                        print(last_word)
            else:
                rand = random.randint(0, length)
                last_word = (list(self.states)[rand])

            sentence.append(last_word)

            if num_words < sent_length:
                add_words = False

            
        space = ' '
        sentence = space.join(sentence)

        return sentence


if __name__ == '__main__':
    source = 'one fish two fish red fish blue fish'
    markov = Markov('source.txt')
    # print(markov.states)
    # print('')
    print(markov.random_walk())

