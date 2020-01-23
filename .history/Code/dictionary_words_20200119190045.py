import random


def random_words(num):
    ''' uses words list in Unix
    takes in a number returns a sentence 
    from the word list of random order 
    with the number of words inputted
    '''

    wl = open('/usr/share/dict/words', 'r')
    word_list = wl.read()
    wl.close()

    print(word_list)

    length = len(word_list)
    sentence = []

    for word in range(num):
        rand_num = random.randint[0, length]
        new_word = word_list[rand_num]
        sentence.append(new_word)

    print(sentence)
    return 

if __name__ == '__main__':
    random_words(4)