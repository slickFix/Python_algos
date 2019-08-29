class Node:

    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None

def printBFT(root):

    q = []
    q.append(root)

    while len(q) >0:
        node = q.pop(0)
        print(node.val,end=' ')

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    print()

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Level Order Traversal of binary tree is -")
    printBFT(root)
