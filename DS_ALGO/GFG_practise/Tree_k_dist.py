class Node:

    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def print_k_dist(root,k):

    if root is None:
        return

    if k == 0:
        print(root.data,end= ' ')
        return

    print_k_dist(root.left,k-1)
    print_k_dist(root.right,k-1)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(8)

    print_k_dist(root, 2)