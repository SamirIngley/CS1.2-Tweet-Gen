
def list_histo(source):
    histo = []

    text = source.split()
    
    print(text)
    for word in text:
        instance = [word, 1]
        for item in histo:
            print(word)
            if word not in item:
                histo.append(instance)
            else:
                item[1] += 1


    print(histo)
    return histo







if __name__ == '__main__':
    source = 'one fish two fish red fish blue fish'
    list_histo(source)