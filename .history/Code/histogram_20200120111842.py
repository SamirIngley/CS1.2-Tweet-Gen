
def list_histo(source):
    histo = []

    text = source.split()
    
    print(text)

    current = word 
    for word in text:
        counter = 1
        for word2 in text:
            if word == word2:
                counter += 1
    instance = [word, counter]
        
            
             


    print(histo)
    return histo







if __name__ == '__main__':
    source = 'one fish two fish red fish blue fish'
    list_histo(source)