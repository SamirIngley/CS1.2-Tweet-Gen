import random
import sys

def dictionary_words(num):
    file = open("/usr/share/dict/words", "r")
    words_list = (file.read().split('\n')) #.read gives whole file, .split splits a string into a list 
    # print(words_list)
    new_list = []
    length = len(words_list)

    for word in range(num):
        rand_num = random.randint(0, length)
        new_word = words_list[rand_num]
        new_list.append(new_word)
    
    return (' '.join(new_list))



if __name__ == '__main__':
    args = sys.argv
    # print(args[1:]) # list
    print(dictionary_words(int(args[1:][0])))