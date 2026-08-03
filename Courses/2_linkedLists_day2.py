class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

        

    def addValue(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete_value(self, value):
        current = self.head
        previous = None

        if self.head == None:
            return "List is Empty"
        

        if self.head.data == value:
            self.head = self.head.next
            return
        
        while current != None:
            if current.data == value:
                previous.next = current.next
                return "Deleted"
            else:
                previous = current
                current = current.next

        


    def find_value(self, value):

        current = self.head
        while current != None:
            if current.data == value:
                return "found"
            else:
                current = current.next
        return "Not Found"
            


    def printList(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

new_list = LinkedList()
new_list.addValue(2)
new_list.addValue(4)
new_list.addValue(3)


new_list.delete_value(4)
new_list.printList()
print(new_list.find_value(4))

