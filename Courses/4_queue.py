class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return


        self.tail.next = new_node
        self.tail = new_node
        


    def dequeue(self):
        current = self.head
        if current == None:
            return  "list is Empty"
        
        dequeued = self.head.data
        self.head = self.head.next

        return dequeued


# head(1) -> tail -> tail(3)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # expected 1
print(q.dequeue())  # expected 2
print(q.dequeue())  # expected 3
print(q.dequeue())  # expected "list is Empty"