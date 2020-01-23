
def list_histo(source):
    histo = []

    text = source.split()
    
    print(text)
    for word in text:
        instance = [word, 1]
        if instance not in histo:
            histo.append(instance)
        else: 
            for item in histo:
                if word == item[0]:
                    item[1] += 1
            
             


    print(histo)
    return histo







if __name__ == '__main__':
    source = 'one fish two fish red fish blue fish'
    list_histo(source)