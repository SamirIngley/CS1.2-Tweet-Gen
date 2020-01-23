
def list_histo(source):
    histo = []

    text = source.split()

    for word in text:
        for item in histo:
            if word == item[1]:
                item[0] += 1
            else:
                histo.append([1, word])

    print(histo)
    return histo


if __name__ == '__main__':
    source = 'one fish two fish red fish blue fish'
    list_histo(source)