# Inserting Vaules in BST(Binary Search Tree)

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None



    def inorder(self, node):
        if node is None:    # base case — stop here 
            return
        
        self.inorder(node.left)   # go LEFT first
        print(node.data)      # visit ROOT
        self.inorder(node.right)   # go RIGHT last


    def preorder(self, node):
        if node is None:
            return
        
        print(node.data)
        self.preorder(node.left)
        self.preorder(node.right)


    def postoder(self, node):
        if node is None:
            return
        self.postoder(node.left)
        self.postoder(node.right)
        print(node.data)

    def insertion(self, value):
        new_node = TreeNode(value)
        if self.root == None:
            self.root = new_node
            return              # ✅ stop here

        current = self.root
        while True:
            if value < current.data:
                if current.left == None:
                    current.left = new_node  # ✅ node not value
                    return                    # ✅ stop after inserting
                current = current.left
            elif value > current.data:
                if current.right == None:
                    current.right = new_node  # ✅ node not value
                    return                     # ✅ stop after inserting
                current = current.right


tree = BinaryTree()
tree.insertion(10)
tree.insertion(5)
tree.insertion(15)
tree.insertion(3)
tree.insertion(7)
tree.insertion(8)

print(tree.root.data)
# tree.inorder(tree.root)