import sample
from clean_text import clean

class Markov():
    def __init__(self, corpus):
        self.corpus = corpus
        self.states = {}
        self.chain()
    
    def chain(self):
        last_word = None

        for word in self.corpus:
            if last_word is not None:
                if word not in self.states:
                    self.states[last_word] = Dictogram()
                self[last_word].add_count(word)
            last_word = word

        
        return chain

if __name__ == '__main__':
    source = 'one fish two fish red fish blue fish'
    print(markov(source))