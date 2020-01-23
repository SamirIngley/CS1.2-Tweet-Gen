

file = open('words', 'w')
print(file[0:10])

wl = open('/usr/share/dict/words', 'r')
wordlist = wl.readlines()
wl.close()

