import sample

def markov(source):

    chain = {}

    prev = None
    current = None

    for word in source:
        current = word
        if not chain:
            chain[current] = None
        if word not in chain:
            chain[word] = None 
        


        prev = current

    current = None
    prev = None

    for word in source:
        current = word

        if not chain:
            chain[current]
        
        chain[prev] += current
        
        prev = current