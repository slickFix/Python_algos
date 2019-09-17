class Node:
    def __init__(self,data):
        self.key = data
        self.right = self.left = None


def lca(root, n1, n2):
    '''
    :param root: given root of the bst
    :param n1: value one.
    :param n2: value two.
    :return: Lowest common Ancestor key.
    '''

    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root.key

    l_ret = lca(root.left, n1, n2)
    r_ret = lca(root.right, n1, n2)

    if l_ret is not None and r_ret is not None:
        return root.key

    elif l_ret is None:
        return r_ret

    else:
        return l_ret

if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    n1 = 10;
    n2 = 14
    t = lca(root, n1, n2)
    print("LCA of %d and %d is %d" % (n1, n2, t.data))

    n1 = 14;
    n2 = 8
    t = lca(root, n1, n2)
    print("LCA of %d and %d is %d" % (n1, n2, t.data))

    n1 = 10;
    n2 = 22
    t = lca(root, n1, n2)
    print("LCA of %d and %d is %d" % (n1, n2, t.data))
