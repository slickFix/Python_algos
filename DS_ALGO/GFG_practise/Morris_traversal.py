class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def morris_inorder(root):

    current = root

    while current is not None:

        pre = current.left

        if pre is None:
            print(current.data,end=' ')
            current = current.right

        else:

            while pre.right is not None and pre.right !=current:
                pre = pre.right

            if pre.right is None:
                pre.right = current
                current = current.left

            else:
                pre.right = None
                print(current.data,end= ' ')
                current = current.right

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    morris_inorder(root)

