class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def checkBST(root,minV,maxV):

    if root is None:
        return True

    if root.data < minV or root.data > maxV:
        return False

    return checkBST(root.left,minV,root.data -1 ) and checkBST(root.right,root.data+1,maxV)

if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    if (checkBST(root,-4294967296,4294967296)):
        print("Is BST")
    else:
        print("Not a BST")
