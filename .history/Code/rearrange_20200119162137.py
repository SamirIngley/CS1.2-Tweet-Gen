import random

def random_rearrange(input_string):
    ''' Asks user for input of words, then 
    rearranges those words in a random order
    '''
    # input_string = input("enter words: ")
    words = input_string.split(' ')

    len_words = len(words)
    # print(words)
    word_list = []

    for word in range(len_words):
        rand = random.randint(0,len_words-1)
        # print(rand)
        word_list.append(words[rand])    
    # print(word_list)

    space = ' '
    sentence = space.join(word_list)
    print(sentence)
    return sentence


def reverse_order(input_string):
    ''' 
    Reverses the order or words inputted by user
    '''

    # input_string = input("enter words: ")
    words = input_string.split(' ')
    print(words)

    length = len(words) - 1
    word_list = []

    for word in words:
        word_list.append(words[length])
        length -= 1
    print(word_list)

    space = ' '
    sentence = space.join(word_list)
    print(sentence)
    return sentence


def mad_libs():
    nouns_string = input('Give me a noun: ')
    names_string = input('Give me a name: ')
    verbs_string = input('Give me two verbs: ')
    
    nouns = nouns_string.split(' ')
    names = names_string.split(' ')
    verbs = verbs_string.split(' ')
    print(verbs)

    print("One day I went to the store to buy myself a {}.".format(nouns[0]))
    print("'What's the matter with you {}?' The clerk asked.".format(names[0]))
    print("'This fits me well' I said")
    print("'Well go on then {} it out so you don't miss out.".format(verbs[0]))
    print("'Let me {} first and I'll give you what I have.'".format(verbs[1]))

# def anagram():
#     ''' handshake with each letter 
#     rearrange to see every possible combination of words
#     '''
#     word = input('Letters/word: ')
#     length = len(word)
#     current = None
#     temp = None
#     for letter in word:
#         current = letter 
#         for letter2 in word:
#             temp = letter2
#             if letter == letter2:
#                 pass
#             else:
    
def anagram(input_string):
    ''' takes a word and returns every possible combination of letters
    '''
    word_string = input_string
    new_strings = []
    linked_list = LinkedList()
    linked_list_swaps = LinkedList()
    linked_list.read()
    linked_list_swaps.read()


    for letter in input_string:
        linked_list.insert(letter)
        linked_list_swaps.insert(letter)

    linked_list.read()
    print(len(word_string))
    index = 0
    while index < len(word_string):
        for letter in word_string:
            for letter2 in word_string:
                linked_list_swaps.swap(letter, letter2)
                new_strings.append(linked_list.read() + "\n")
                linked_list_swaps.swap(letter2, letter)
                index += 1

    linked_list_swaps.read()
    print(new_strings)
    return 
    


class Node():
    def __init__(self, data=None, next_pointer=None):
        self.data = data    
        self.next_pointer = next_pointer
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_pointer

    def set_next(self, next_node):
        self.next_pointer = next_node

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found == False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if current == None:
            return ValueError("does not exist")
        if previous == None:
            self.head = current.get_next() 
        if found == True:
            previous.set_next(current.get_next())

    def read(self):
        current = self.head
        read = []
        while current:
            data = current.get_data()
            read.append(data)
            current = current.get_next()
        
        no_space = ''
        sentence = no_space.join(read)
        print(sentence)
        return 


    def swap(self, data1, data2):
        node1 = None
        node2 = None
        current = self.head
        
        if data1 == data2:
            print("n/a")
            return 
        
        while current:
            curr_data = current.get_data()
            if  curr_data == data1:
                node1 = current
            elif curr_data == data2:
                node2 = current 
            current = current.get_next()
        
        temp1 = node1.get_data()
        temp2 = node2.get_data()

        node1.data = temp2
        node2.data = temp1
        return 

        

    def size(self):
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.get_next()
        print(counter)
        return counter


if __name__ == '__main__':
    # input_string = 'hello yellow fellow'
    # random_rearrange(input_string)
    # reverse_order()
    # mad_libs()

    linked_list = LinkedList()
    linked_list.insert('a')
    linked_list.insert('b')
    linked_list.insert('c')
    linked_list.insert('d')
    linked_list.insert('e')
    linked_list.insert('f')
    linked_list.insert('g')
    linked_list.insert('h')
    linked_list.insert('i')
    linked_list.insert('j')
    linked_list.insert('k')
    linked_list.read()

    linked_list.delete('a')
    linked_list.read()

    print(range(linked_list.size()))

    linked_list.swap([0],[10])
    linked_list.read()