class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        # Currently the new_node is not connected to any head or tail. also our first node has
        # no value hence no tail to be linked to this head node:
        if self.head is None:
            self.head = new_node
            print("Head Node created: ", self.head.value)
            return
        # by adding this line we check if the first node is = None
        # we make it equal to the next node

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Appended new Node with value: ", node.next.value)


llist = LinkedList()
llist.append("First Node")
llist.append("Second Node")
llist.append("Third Node")

