
def list_histo(source):
    histo = []

    text = source.split()

    for word in text:
        if word in histo:
            word[0] += 1
        else:
            histo.append([1, word])


    return histo


if __name__ == '__main__'
    source = 'one fish two fish red fish blue fish'
    histogram(source)