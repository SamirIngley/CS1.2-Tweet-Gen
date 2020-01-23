

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

def dict_hist(source):
    ''' Dictionary key value pairs {'hello':1, 'sir':2, 'how':5}
    Takes text. Stores each item in text, compares each item to the rest of the words in 
    text and keeps a running total. Used list account for no repeats.'''

    histo_dict = {}
    used = []

    text = source.split()
    # print(text)

    for word in text:
        if word in histo_dict:
            histo_dict[word] += 1
        else:
            histo_dict[word]
        

    print(histo_dict)
    return histo_dict

def counts_list(source):

    histo = []
    instances = []
    used = []

    text = source.split()
    # print(text)

    for word in text:
        # check if the word has already been accounted 
        if word in used:
            continue

        counter = 0
        used.append(word)
        # for each word in the text if it matches a word in the same text, 
        # we have an instance of that word - so increase counter by 1
        for word2 in text:
            if word == word2:
                counter += 1
        # we know the word and we have the occurances stored in counter. 
        # create a list instance object with the word and its occurances 
        # and append it to the list of word instances.  
        instance = [word, counter]
        instances.append(instance)
    
    used_nums = []
    for item in instances:
        #  check if the word frequency has been accounted for before
        if item[1] in used_nums:  
            continue
        used_nums.append(item[1])
        membs = [] 
        new_instance = (item[1], membs) # this is what an instance of our histogram looks like
        # for one item in our instances we check if the frequency matches
        # any other frequencies in the instances list. if it does we add those to members list
        for item2 in instances: 
            if item[1] == item2[1]:
                # print(item2[0])
                membs.append(item2[0])
        
        histo.append(new_instance)

    print(histo)
    return histo







if __name__ == '__main__':
    source = 'one fish two fish red fish blue fish'
    list_hist(source)
    tuple_hist(source)
    dict_hist(source)
    counts_list(source)
   