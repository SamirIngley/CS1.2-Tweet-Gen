
class Node(object):
    
    def __init__(self, data, next = None, prev = NotImplemented):
        self.next = next
        self.prev = prev
        self.data = None