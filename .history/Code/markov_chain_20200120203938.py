import sample
from clean_text import clean

def markov(source):

    text = source.split()

    chain = {}

    current = None
    prev = None

    for word in text:
        current = word

        if not chain:
            chain[current] = None
        else:
            chain[prev] = current

        prev = current
    
    return chain

if __name__ == '__main__':
    # source = 'one fish two fish blue fish'
    print(markov(source.txt))