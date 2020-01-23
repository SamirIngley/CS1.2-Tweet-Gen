
def random_words(num):

    wl = open('/usr/share/dict/words', 'r')
    wordlist = wl.readlines()
    wl.close()