class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def height(root):

    if root is None:
        return 0

    lh = height(root.left)
    rh = height(root.right)

    return max(lh,rh) + 1

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Height of tree is %d" % (height(root)))