import random
from clean_text import clean
from dictogram import Dictogram

''' General vocab:
Stack : Last in First Out
Queue : First in First out
For a markov chain of n length we want to use a queue. Where we store the length n words and 
add the next word while removing the last word to traverse the corpus and save the states. 
'''

class Markov():
    def __init__(self, corpus):
        self.corpus = clean(corpus)
        self.states = {}
        self.chain()
    
    def chain(self):

        
        # build the chain with states
        queue = []
        prev_q = []

        for word in self.corpus:
        
            while len(queue) < 2:
                queue.append(word)
            
            tup = tuple(prev_q)
            tup_q = tuple(queue)
            if tup is not None:
                if tup not in self.states:
                    self.states[tup] = Dictogram()
                self.states[tup].add_count(tup_q)

            prev_q = queue
            queue.pop(0)

        # last_word = None
 
        # for word in self.corpus:
        #     if last_word is not None: # set last word line 14

        #         if last_word not in self.states: # if we haven't seen this word before
        #             self.states[last_word] = Dictogram() # empty dictogram as value
        #         self.states[last_word].add_count(word) # add word to last word histogram

        #     last_word = word # set word as last_word


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


