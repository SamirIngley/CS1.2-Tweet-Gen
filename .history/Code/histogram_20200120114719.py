

def tuple_hist(source):
    ''' Fastest - tuples are immutable. List of tuples: [('hello', 3), ('what', 4)]
    Takes text. Stores each item in text, compares each item to the rest of the words in 
    text and keeps a running total. Used list account for no repeats.
    '''
    histo = []
    used = []

    text = source.split()
    # print(text)

    for word in text:
        counter = 0
        if word in used:
            continue

        used.append(word)

        for word2 in text:
            if word == word2:
                counter += 1

        instance = (word, counter)
        histo.append(instance)

    print(histo)
    return histo


def list_hist(source):
    ''' List of lists histogram. [['hello', 1], ['you', 3], ['sir', 4]]
    Takes text. Stores each item in text, compares each item to the rest of the words in 
    text and keeps a running total. Used list account for no repeats.
    '''

    histo = []
    used = []

    text = source.split()
    # print(text)

    for word in text:
        counter = 0
        if word in used:
            continue

        used.append(word)

        for word2 in text:
            if word == word2:
                counter += 1
            
        instance = [word, counter]
        histo.append(instance)

    print(histo)
    return histo






if __name__ == '__main__':
    source = 'one fish two fish red fish blue fish'
    list_hist(source)
    tuple_hist(source)
   