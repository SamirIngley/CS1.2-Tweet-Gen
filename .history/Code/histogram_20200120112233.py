
def list_histo(source):
    histo = []
    used = []

    text = source.split()
    
    print(text)

    for word in text:
        counter = 0
        if word in used:
            continue

        used.append(word)
        
        for word2 in text:
            if word == word2:
                counter += 1
            
        instance = [word, counter]
        histo.append(instance)

    print(histo)
    return histo







if __name__ == '__main__':
    source = 'one fish two fish red fish blue fish'
    list_histo(source)