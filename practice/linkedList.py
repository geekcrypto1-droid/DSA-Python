class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    
    def insert_at_beginning(self, value):
        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        current = self.head
        new_node = Node(value)

        if current == None:
            new_node.next = current
            self.head = new_node
            return

        while current.next != None:
            current = current.next
        new_node.next = None
        current.next = new_node


    def find_value(self, value):
        current = self.head
        while current != None:
            if current.data == value:
                return "Found"
            current = current.next
        
        return "Not Found"
    

    def print_list(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next



new_list = LinkedList()
new_list.insert_at_end(5)
new_list.insert_at_end(10)
new_list.insert_at_beginning(10)
new_list.insert_at_beginning(20)
new_list.insert_at_end(0)
new_list.print_list()
print(new_list.find_value(10))
print(new_list.find_value(99))
