class Node:

    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None

def inorder(root):

    if root is None:
        return

    inorder(root.left)
    print(root.val,end=' ')
    inorder(root.right)

def preorder(root):

    if root is None:
        return

    print(root.val,end=' ')
    preorder(root.left)
    preorder(root.right)

def postorder(root):

    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.val,end=' ')


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Preorder traversal of binary tree is")
    preorder(root)

    print("\nInorder traversal of binary tree is")
    inorder(root)

    print("\nPostorder traversal of binary tree is")
    postorder(root)
