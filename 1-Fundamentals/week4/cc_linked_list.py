class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            print("New Node Created! Value: ", self.head.value)
            return
        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Appended new Node with value: ", node.next.value)

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            print("New Node Created! Value: ", self.head.value)
            return
        node = self.head
        if node is not None:
            previous_node = self.head
            self.head = new_node
            self.head.next = previous_node

        print("Prepended new Head Node with value: ", self.head.value)
        print("Node following Head is: ", previous_node.value)


llist = Linkedlist()
llist.prepend("First Node")
llist.prepend("Inserted New First Node")


