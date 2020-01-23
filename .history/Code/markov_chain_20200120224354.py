import sample
from clean_text import clean

def markov(source):

    # text = clean(source)
    text = source.split()
    print(text)
    chain = {}

    for word in text:

        if word not in self.states:
            self[word] = Dictogram()
        self[word].add_count()

    
    return chain

if __name__ == '__main__':
    source = 'one fish two fish red fish blue fish'
    print(markov(source))