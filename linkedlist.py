from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """

        # TODO: Write function to prepend here
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            self.head = Node(value)
            self.head.next = current
        return self.head

    def append(self, value):
        """ Append a value to the end of the list. """

        # TODO: Write function to append here
        current = self.head
        if self.head:
            while current.next:
                current= current.next
            current.next = Node(value)
        else:
            self.head = Node(value)
        return self.head

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """

        # TODO: Write function to search here
        current = self.head
        if self.head:
            while current.value is not value:
                current = current.next
            return current
        return None

    def remove(self, value):
        """ Remove first occurrence of value. """

        # TODO: Write function to remove here
        current = self.head.next
        prev = self.head
        if self.head.value == value:
            self.head = self.head.next
            return self.head
        while current is not None and current.value != value:
            prev = current
            current = current.next
        current = current.next
        prev.next = current
        return self.head

    def pop(self):
        """ Return the first node's value and remove it from the list. """

        # TODO: Write function to pop here
        if self.head:
            current = self.head.value
            self.head = self.head.next
            return current
        return None

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """

        # TODO: Write function to insert here
        node = self.head
        if size(self) < pos:
            while node is not None:
                node = node.next
            node = Node(value)
        else:
            size = 0
            prev = self.head
            while node is not None:
                size+=1
                if size == pos:
                    current = node

        pass

    def size(self):
        """ Return the size or length of the linked list. """


        # TODO: Write function to get size here
        size = 0
        node = self.head
        while node is not None:
            size += 1
            node = node.next
        return size

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out
