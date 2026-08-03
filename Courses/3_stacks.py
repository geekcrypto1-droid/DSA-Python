class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class Stacks:
    def __init__(self):
        self.head = None

    
    def push(self, value):
        new_node = Node(value)
        current = self.head

        new_node.next = current
        self.head = new_node

    def pop(self):
        if self.head == None:
            return "list is empty"

        popped = self.head.data 
        self.head = self.head.next
        return popped
    

my_stack = Stacks()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())