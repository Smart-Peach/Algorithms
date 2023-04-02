class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_end(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        last_node = self.head
        while(last_node.next):
            last_node = last_node.next
        last_node.next = node



