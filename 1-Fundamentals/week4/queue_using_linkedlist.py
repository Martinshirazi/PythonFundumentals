class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_nodes = 0

    def size(self):
        return self.num_nodes

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None:
            # self.head = new_node
            # self.tail = new_node
            self.head = self.tail = new_node  # same as above two lines

        else:
            self.tail.next = new_node
            self.tail = new_node

        self.num_nodes += 1

    def dequeue(self):
        if self.head is None:
            return None

        dequeue_node_value = self.head.value
        self.head = self.head.next
        self.num_nodes -= 1
        return dequeue_node_value


q = Queue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
q.enqueue("d")

print("Pass" if (q.size() == 4) else "Fail")
q.enqueue('e')
print("Pass" if (q.size() == 5) else "Fail")

print("Pass" if (q.dequeue() == 'a') else "Fail")
print("Pass" if (q.dequeue() == 'e') else "Fail")  # this statement returns Fail because next item to dequeue is "b"
# not "d", but still B will be removed and hence the next statement returns Pass!
print("Pass" if (q.size() == 3) else "Fail")
