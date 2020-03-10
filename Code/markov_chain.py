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
        # self.corpus = corpus
        self.states = {}
        self.chain()
        # self.size = size
    
    def chain(self):
        ''' Nth order markov chain '''
        
        # build the chain with states
        queue = []
        prev_q = []

        for word in self.corpus:
            
            print(word)
            if len(queue) < self.size:
                queue.append(word)
                continue
            
            tup_q = tuple(queue)
            # print('queue: ', tup_q)

            if len(prev_q) > 0:
                if tup_p not in self.states:
                    self.states[tup_p] = Dictogram()
                self.states[tup_p].add_count(tup_q)

            prev_q = queue
            tup_p = tuple(prev_q)
            # print('prev: ', tup_p)

            queue.pop(0)
            queue.append(word)


        # ------------------FIRST ORDER MARKOV ----------------
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

            sentence.append(last_word[-1])

        space = ' '
        sentence = space.join(sentence)
        
        return sentence

if __name__ == '__main__':
    # source = 'one fish two fish red fish blue fish'
    # markov = Markov('I went right, he went left. I went right, I went left')
    markov = Markov('source.txt', 4)
    print(markov.states)
    # print('')
    # print(markov.chain())
    print(markov.random_walk(13))
    # print(markov.__str__())
    # rand = random.randint(0, 2000)
    # print(rand)


