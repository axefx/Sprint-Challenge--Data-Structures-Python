class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # traverse
        # set current head
        current = self.head
        # traverse while current head is not None
        while current is not None:
            # get next node
            next = current.next_node
            # replace currents next node to previous node
            current.next_node = prev
            # set current to previous node
            prev = current
            # update current to traverse to next node
            current = next
        # update head
        self.head = prev
