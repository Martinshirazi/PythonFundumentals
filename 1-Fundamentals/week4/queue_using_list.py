class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


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
q.show_queue()