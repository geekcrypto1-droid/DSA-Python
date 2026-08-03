# find Depth of a linked tree

# 8 <- 10 -> 15

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
        current = self.root
        
        if current == None:
            self.root = new_node
            return
        
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

        depth = 1 + max(left, right)
        return depth
    

    def inorder(self, node):
        if node == None:
            return "list is Empty"
        
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)



def find_similarities(p, q):
    if p is None and q is None:
        return True
    
    if p.data != q.data:
        return False
    
    
    return find_similarities(p.left, q.left) and find_similarities(p.right, q.right)

tree1 = TreeList()
tree1.insert_value(10)
tree1.insert_value(15)
tree1.insert_value(8)



tree2 = TreeList()
tree2.insert_value(10)
tree2.insert_value(8)
tree2.insert_value(14)

print(find_similarities(tree2.root, tree1.root))