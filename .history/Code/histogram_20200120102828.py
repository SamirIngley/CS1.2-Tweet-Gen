
def list_histo(source):
    histo = []

    text = source.split()
    
    print(text)
    for word in text:
        instance = [word, 1]
        if len(histo) == 0:
            histo += instance
            continue
        for item in histo:
            print(word)
            if word == item[1]:
                item[0] += 1
            else:
                histo += instance


    print(histo)
    return histo







if __name__ == '__main__':
    source = 'one fish two fish red fish blue fish'
    list_histo(source)