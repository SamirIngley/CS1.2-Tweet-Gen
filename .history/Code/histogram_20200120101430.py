
def list_histo(source):
    histo = []

    text = source.split()
    print(text)
    for word in text:
        print(word)
        for item in histo:
            print(item)
            if word == item[1]:
                item[0] += 1
            else:
                histo.append(1, word)


    print(histo)
    return histo







if __name__ == '__main__':
    source = 'one fish two fish red fish blue fish'
    list_histo(source)