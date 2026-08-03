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


tree = BinaryTree()
tree.root = TreeNode(10)
tree.root.left = TreeNode(5)
tree.root.right = TreeNode(15)
tree.root.left.left = TreeNode(3)
tree.root.left.right = TreeNode(7)

print("Inorder:")
tree.inorder(tree.root)      # expected: 3 5 7 10 15
print("Preorder:")
tree.preorder(tree.root)     # expected: 10 5 3 7 15
print("Postorder:")
tree.postoder(tree.root)    # expected: 3 7 5 15 10