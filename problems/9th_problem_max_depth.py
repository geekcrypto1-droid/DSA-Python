class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class TreeList:
    def __init__(self):
        self.root = None

    def insert_value(self, value):
        new_node = TreeNode(value)
        if self.root == None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if value < current.data:
                if current.left == None:
                    current.left = new_node
                    return
                current = current.left

            elif value > current.data:
                if current.right == None:
                    current.right = new_node
                    return
                current = current.right

    def find_depth(self, node):
        if node == None:
            return 0
        
        left = self.find_depth(node.left)
        right = self.find_depth(node.right)
        return 1 + max(left, right)

            


    def inorder(self, node):
        if node == None:    # base case — stop here 
            return
        
        self.inorder(node.left)   # go LEFT first
        print(node.data)      # visit ROOT
        self.inorder(node.right)   # go RIGHT last



new_tree = TreeList()
new_tree.insert_value(2)
new_tree.insert_value(8)
new_tree.insert_value(0)
new_tree.insert_value(5)
new_tree.insert_value(1)
new_tree.insert_value(4)

# print(new_tree.root.left.right.data)

# new_tree.inorder(new_tree.root)
print(new_tree.find_depth(new_tree.root))