class Node:
    def __init__(self,data):
        self.key = data
        self.right = self.left = None


def find_min(node):
    curr = node
    while curr.left is not None:
        curr = curr.left
    return curr


def deleteNode(root,key):

    if root is None:
        return None

    if root.key < key:
        root.right = deleteNode(root.right,key)
    elif root.key > key:
        root.left = deleteNode(root.left,key)
    else:

        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            node = find_min(root.right)
            root.key = node.key
            root.right = deleteNode(root.right,node.key)
    return root


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key,end=' ')
        inorder(root.right)


def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)

        # Otherwise recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

        # return the (unchanged) node pointer
    return node

if __name__ == '__main__':
    """ Let us create following BST 
                  50 
               /     \ 
              30      70 
             /  \    /  \ 
           20   40  60   80 """

    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    print("Inorder traversal of the given tree")
    inorder(root)

    print("\nDelete 20")
    root = deleteNode(root, 20)
    print("Inorder traversal of the modified tree")
    inorder(root)

    print("\nDelete 30")
    root = deleteNode(root, 30)
    print("Inorder traversal of the modified tree")
    inorder(root)

    print("\nDelete 50")
    root = deleteNode(root, 50)
    print("Inorder traversal of the modified tree")
    inorder(root)


