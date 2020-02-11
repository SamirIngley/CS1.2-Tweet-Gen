from clean_text import clean
from benchmark import bench

def tuple_hist(source):
    ''' Fastest - tuples are immutable. List of tuples: [('hello', 3), ('what', 4)]
    Takes text. Stores each item in text, compares each item to the rest of the words in 
    text and keeps a running total. Used list account for no repeats.
    '''
    histo = []
    used = []
    # text = source.split()
    text = clean(source)
    # print(text)
    for word in text:
        # see if we've used the word before
        counter = 0
        if word in used: 
            continue
        
        used.append(word)
        for word2 in text: 
            if word == word2:
                counter += 1

        instance = (word, counter)
        histo.append(instance)

    # print(histo)
    # print('USED: ', used)
    return histo


def list_hist(source):
    ''' List of lists histogram. [['hello', 1], ['you', 3], ['sir', 4]]
    Takes text. Stores each item in text, compares each item to the rest of the words in 
    text and keeps a running total. Used list account for no repeats.
    '''

    histo = []
    used = []

    text = clean(source)

    # print(text)

    for word in text: 
        counter = 0
        if word in used:
            continue
        
        used.append(word)

        for word2 in text: #source to text
            if word == word2:
                counter += 1
        
        instance = [word, counter]
        histo.append(instance)

    # print(histo)
    return histo

def dict_hist(source):
    ''' Dictionary key value pairs {'hello':1, 'sir':2, 'how':5}
    Takes text. Stores each item in text, compares each item to the rest of the words in 
    text and keeps a running total. Used list account for no repeats.'''

    histo_dict = {}
    # used = []

    text = clean(source)
    # print(text)

    for word in text:
        if word in histo_dict:
            histo_dict[word] += 1
        else:
            histo_dict[word] = 1
        
    # print(histo_dict)
    return histo_dict


def counts_list(source):

    histo = []
    instances = []
    used = []

    text = clean(source)
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

    # print(histo)
    return histo



def unique_words(histo):
    ''' takes a histogram and returns the number of unique words in it.
    '''
    return len(histo)
    # counter = 0
    # for item in histo:
    #     if type(item[0]) == int: # if the first item is an integer
    #         for word in item[1]:
    #             # print(item[1])
    #             counter += 1
    #     else:
    #         # print(item)
    #         counter += 1
    # # print(counter)
    # return counter

def frequency(word, histo):
    ''' takes a word and histo, returns the frequency of that word in the histo
    '''
    return histo[word]
    # for item in histo:
    #     if word in item:
    #         freq = 0
    #         if type(item[0]) == int: # if the first item is an integer
    #             freq = item[0]
    #         else:
    #             freq = item[1]
    #         # print("{} freq: {}".format(word, freq))
    #         return freq





if __name__ == '__main__':
    # source = 'one fish two fish red fish blue fish'
    listo_histo = list_hist("source.txt")
    print(listo_histo)
    tuple_histo = tuple_hist("source.txt")
    print(tuple_histo)
    # print(dict_hist('source.txt'))
    # print(counts_list('source.txt'))
    # print('')
    print(unique_words(list_hist("source.txt")))
    # print(unique_words(counts_list('source.txt')))
    print('freq of fish: ', frequency('the', list_hist("source.txt")))
    # print('freq of tax: ', frequency('tax', list_hist("source.txt")))
    # print('freq of i: ', frequency('i', list_hist("source.txt")))
    # print('benchmark for list hist: ', bench(listo_histo))
    # print('benchmark for dict hist: ', bench(dict_hist('source.txt')))
    # print('benchmark for tuple hist: ', bench(tuple_histo))
