
class Node(object):
    
    def __init__(self, data, next_node=None, prev_node=None):
        ''' Initialize previous node for doubly linked list''' 
        self.next_node = next_node
        self.prev_node = prev_node
        self.data = data
    
    def __repr__(self):
        ''' Return a string representation of node'''
        return 'Node({!r})'.format(self.data)

class Doubly(object):

    def __init__(self, items=None):
        self.head = None
        self.tail = None
        self.length = 0

        if items:
            for item in items:
                self.append(item)
        
