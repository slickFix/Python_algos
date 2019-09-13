class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def insert(root,data):

    if root is None:
        return Node(data)

    else:

        if data > root.data:
            root.right = insert(root.right,data)
        elif data < root.data:
            root.left = insert(root.left,data)
        else:
            return root

        return root


def minValue(root):

    curr = root

    while curr.left is not None:
        curr = curr.left

    return curr.data

if __name__ == '__main__':
    root = None
    root = insert(root, 4)
    insert(root, 2)
    insert(root, 1)
    insert(root, 3)
    insert(root, 6)
    insert(root, 5)

    print("\nMinimum value in BST is %d" % (minValue(root)))
