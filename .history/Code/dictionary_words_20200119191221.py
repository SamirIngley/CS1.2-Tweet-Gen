import random

def dictionary_words(num):
    file = open("/usr/share/dict/words", "r")
    words_list = (file.read().split('\n')) #.read gives whole file, .split splits a string into a list 
    # print(words_list)
    new_list = []

    # for word in range(num):
    #     new_list.append(random.choice(words_list))
    # return(' '.join(new_list))

    length = len(words_list)

    for word in range(num):
        rand_num = random.randint(0, length)
        new_word = words_list[rand_num]
        print(rand_num)
        print(new_word)
        # new_list.append(new_word)



if __name__ == '__main__':
    print(dictionary_words(3))