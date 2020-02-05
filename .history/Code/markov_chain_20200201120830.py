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

        if last_word not in self.states: # if we haven't seen this word before
            self.states[last_word] = Dictogram() # empty histogram as value
        self.states[last_word].add_count(word) 
             
    def __str__(self):
        return str(self.states)


    def random_walk(self, num_words=15):
        
        sentence = []

        length = len(self.states)

        last_word = None

        while len(sentence) < num_words:            
            # print(sentence)
            # print(last_word)
            if last_word: # selects word based on probabilities
                 # dictionary of words to pick from based on last_word's hist
                if last_word in self.states.keys():
                    pickings = self.states[last_word] # dictionary of words to pick from based on last_word's hist
                    total_wc = 0 # number of words in dictionary for last word
                    for value in pickings.values(): # calculates total word count
                        total_wc += value
                        # print(value)
                    # print('last word ', last_word)
                    # print(pickings)
                    # print('total_wc ', total_wc)
                    dart = random.randint(0, 100) # dart as percentage
                    # print('dart ', dart)
                    counter = 0
                    while counter < dart: # when we cross the dart, we've passed the value, so the key stored is the winner
                        for key,value in pickings.items():  # number of times each word appears
                            # print(key, value)
                            counter += (value / total_wc) * 100 # add number of times each word appears til we hit the dart
                            # print('counter ', counter)
                            last_word = key # set last_word to the key
                            # print(last_word)
                else:
                    return
                #     rand = random.randint(0, length-1)
                #     last_word = (list(self.states)[rand])
                    # sentence.append(".")

            else: # assign a last word
                rand = random.randint(0, length-1)
                last_word = (list(self.states)[rand])
                # print(last_word)

            sentence.append(last_word)
            # print(len(sentence))
            
        space = ' '
        sentence = space.join(sentence)

        return sentence


if __name__ == '__main__':
    source = 'one fish two fish red fish blue fish'
    markov = Markov('source.txt')
    # print(markov.states)
    # print('')
    # print(markov.chain())
    print(markov.random_walk(22))
    # rand = random.randint(0, 2000)
    # print(rand)


