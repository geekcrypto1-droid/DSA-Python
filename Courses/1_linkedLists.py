class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    
    def find_value(self, value):
        current = self.head
        while current != None:
            if current.data == value:
                return "Found"
            else:
                current = current.next
        return "Not Found"
    
    def insert_at_beginning(self, value):
        # your code here
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


    def insert_at_end(self, value):
        current = self.head
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            return
                    

        while current.next != None:
            current = current.next
        current.next = new_node            

    def print_list(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next


my_list = LinkedList()
# my_list.insert_at_beginning(30)
# my_list.insert_at_beginning(20)
# my_list.insert_at_beginning(10)
my_list.insert_at_end(40)
my_list.insert_at_end(50)
my_list.insert_at_end(60)

my_list.print_list()
