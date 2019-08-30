class Node:
    def __init__(self,data):

        self.data = data
        self.left = None
        self.right = None

def height(node):

    if node is None:
        return 0

    return 1 + max(height(node.left),height(node.right))

def diameter(node):

    if node is None:
        return 0

    lheight = height(node.left)
    rheight = height(node.right)

    ldia = diameter(node.left)
    rdia = diameter(node.right)

    return max(ldia,rdia,1+lheight+rheight)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Diameter of given binary tree is %d" % (diameter(root)))