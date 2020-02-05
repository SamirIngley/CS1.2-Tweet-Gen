
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
        """Initialize this linked list and append the given items, if any."""

        self.head = None
        self.tail = None
        self.length = 0

        if items:
            for item in items:
                self.append(item)
        
    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(n) Why and under what conditions?
            Because we must loop to the end of the linked list which 
            requires conferring with each node. 
        """
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        node = Node(item)

        if not self.head:
            self.head = node
            self.tail = node
        else: 
            current = self.head
            while current.next: # when current.next does not exit - we've reached the end of the linked list
                current = current.next
            current.next = node
            self.tail = node
        self.length += 1