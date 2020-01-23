import sample

def markov(source):

    chain = {}

    current = None
    prev = None

    for word in source:
        current = word

        if not chain:
            chain[current]
        else:
            chain[prev] += current

        prev = current