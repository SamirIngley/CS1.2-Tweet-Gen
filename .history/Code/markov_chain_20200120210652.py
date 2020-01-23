import sample
from clean_text import clean

def markov(source):

    # text = clean(source)
    text = source.split()
    print(text)
    chain = []

    current = None
    prev = None

    for word in text:
        current = word

        if not chain:
            chain.append[current, None]
        
        for item in chain:
            if item[0] == current:
                item[1] += current
        

        prev = current
    
    return chain

if __name__ == '__main__':
    source = 'one fish two fish red fish blue fish'
    print(markov(source))