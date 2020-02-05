
def get_index(word, listogram):
    current_index = 0
    for item in listogram:
        if item[0] == word:
            return current_index
        current_index += 1
    return -1 # dummy value / this isn't a valid index

def listogram(lines):
    listogram = []
    for word in lines:
        word = word.rstrip()
        index = get_index(word, listogram)
        if index == -1:
            listogram.append([word,1])
        else:
            listogram[index][1] += 1
    return listogram
