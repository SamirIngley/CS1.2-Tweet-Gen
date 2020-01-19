import random
import sys

def random_rearrange():
    words = sys.argv
    print(words)
    word_list = []
    for word in range(6):
        rand = random.randint(0,6)
        word_list.append(words[rand])
    print(word_list)
    return word_list

random_rearrange()