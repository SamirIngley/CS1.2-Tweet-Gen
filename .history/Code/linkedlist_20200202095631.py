#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.length = 0
        # Append given items
        if items is not None:
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

    # def length(self):
    #     """Return the length of this linked list by traversing its nodes.
    #     TODO: Running time: O(n) Why and under what conditions?
    #         Because we have to loop through each node (n number of nodes) until None remain
    #         in the list to get the length. 
    #     """
    #     # TODO: Loop through all nodes and count one for each
    #     counter = 0
    #     node = self.head  # O(1) time to assign new variable
    #     # Loop until node is None, which is one node too far past tail
    #     while node is not None:  # Always n iterations because no early return
    #         counter+=1  # O(1) time (on average) to append to list
    #         # Skip to next node to advance forward in linked list
    #         node = node.next  # O(1) time to reassign variable
    #     return counter

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
        else: 
            current = self.head
            while current.next: # when current.next does not exit - we've reached the end of the linked list
                current = current.next
            current.next = node
        self.length += 1


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) Why and under what conditions?
            Because we can start at the head of the linked list
            and reassign it in the same amount of time everytime.
            Not dependent on number of nodes in the list- we're only concerned
            with self.head
        """
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        node = Node(item)
        node.next = self.head
        self.head = node
        self.length += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) Why and under what conditions?
        self.head is contains the item when quality(item) is True
        TODO: Worst case running time: O(n) Why and under what conditions?
        we must check each node in the whole list of size n. 
        """
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function

        current = self.head

        while current.data != quality(current.data):
            if current.next:
                current = current.next
            else:
                return ('dne')

        return current.data

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O() Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        current = self.head
        prev = None
        found = False

        while not found and current: # find and set the right boundaries to skip
            if current.data != item:
                prev = current
                current = current.next
            else:
                found = True
        self.length -= 1

        if current == None:
            return ValueError('Item not found: {}'.format(item))
        elif prev == None:
            self.head = current.next
        else:
            prev.next = current.next
        return

    def replace(self, item, new_item):
        current = self.head
        found = None
        
        while not found and current:
            if current.data == item:
                found = True
            else:
                current = current.next
        
        if current == None:
            return ValueError('Item not found: {}'.format(item))
        else:
            current.data = new_item

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length)


    for item in ['D', 'E', 'F', 'G']:
        ll.append(item)
    
    print(ll.items())
    ll.replace('F', 'A')
    print(ll.items())

    print(ll.length)


if __name__ == '__main__':
    test_linked_list()
