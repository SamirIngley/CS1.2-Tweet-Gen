import sample

def markov(source):

    chain = {}

    prev = None
    current = None

    for word in source:
        current = word
        instance = [current]
        if not chain:
            chain[current]
        for item in chain:
            if chain


        prev = current