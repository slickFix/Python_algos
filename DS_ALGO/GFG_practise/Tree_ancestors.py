class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def print_ancestors(root,target):

    if root is None:
        return False

    if root.data == target:
        return True

    ret_l = print_ancestors(root.left,target)
    if ret_l:
        print(root.data,end=' ')
        return True
    ret_r = print_ancestors(root.right,target)
    if ret_r:
        print(root.data,end=' ')
        return True

    return False

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(7)

    print_ancestors(root, 7)