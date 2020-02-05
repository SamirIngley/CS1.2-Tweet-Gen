
class Node(object):
    
    def __init__(self, data, next_node=None, prev=NotImplemented):
        self.next_node = next_node
        self.prev = prev
        self.data = None