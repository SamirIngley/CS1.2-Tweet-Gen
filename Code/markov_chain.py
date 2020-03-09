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
                    self.states[last_word] = Dictogram() # empty dictogram as value
                self.states[last_word].add_count(word) # add word to last word histogram

            last_word = word # set word as last_word


        for i,k in zip(self.corpus[0::2], self.corpus[1::2]):  # in the [ ] start at the first value, skip ahead by the last value
            print(i, k)
            
        for i,k in zip(self.corpus, self.corpus[1:]):  # in the [ ] start at the first value, skip ahead by the last value
            print("SECOND VERSION", i, k)

        # current = word
        # if prev != None:

        #     instance = (prev, current)

        #     if instance not in self.states:
        #         self.states[instance] = Dictogram()

        #     if len(self.states) == 0:
        #         continue


                

        #     self.states[instance].add_count()


        # prev = word 

             
    def __str__(self):
        return print(str(self.states))


    def random_walk(self, num_words=15):
        # add code to see what to do if key has no dict. If it's the last word in the sample and is not in gram. 
        sentence = []
        last_word = None
        # print(list(self.states.keys()))
        for i in range(num_words):
            
            if last_word:
                # print(self.states[last_word])
                last_word = self.states[last_word].sample()
            
            else:
                last_word = random.choice(list(self.states.keys()))
                # print(last_word)

            sentence.append(last_word)

        space = ' '
        sentence = space.join(sentence)
        
        return sentence

if __name__ == '__main__':
    source = 'one fish two fish red fish blue fish'
    markov = Markov('source.txt')
    print(markov.states)
    # print('')
    # print(markov.chain())
    print(markov.random_walk(13))
    # print(markov.__str__())
    # rand = random.randint(0, 2000)
    # print(rand)


