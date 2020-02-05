
class Node(object):
    
    def __init__(self, data, next_node=None, prev_node=NotImplemented):
        self.next_node = next_node
        self.prev_node = prev_node
        self.data = None