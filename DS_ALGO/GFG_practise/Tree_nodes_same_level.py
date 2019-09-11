class newnode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.nextRight = None

def connect(root):
    q = []
    prev_ht = 0
    prev_node = None
    q.append((root, 1))

    while len(q) != 0:

        node, ht = q.pop(0)

        if node.left is not None:
            q.append((node.left, ht + 1))

        if node.right is not None:
            q.append((node.right, ht + 1))

        if ht != prev_ht:
            prev_ht = ht
            prev_node = node

        else:
            prev_node.nextRight = node
            prev_node = node

if __name__ == '__main__':

    # Constructed binary tree is
    #         10
    #     / \
    #     8     2
    # /
    # 3
    root = newnode(10)
    root.left = newnode(8)
    root.right = newnode(2)
    root.left.left = newnode(3)

    # Populates nextRight pointer in all nodes
    connect(root)

    # Let us check the values of nextRight pointers
    print("Following are populated nextRight",
          "pointers in the tree (-1 is printed",
          "if there is no nextRight)")
    print("nextRight of", root.data, "is ", end="")
    if root.nextRight:
        print(root.nextRight.data)
    else:
        print(-1)
    print("nextRight of", root.left.data, "is ", end="")
    if root.left.nextRight:
        print(root.left.nextRight.data)
    else:
        print(-1)
    print("nextRight of", root.right.data, "is ", end="")
    if root.right.nextRight:
        print(root.right.nextRight.data)
    else:
        print(-1)
    print("nextRight of", root.left.left.data, "is ", end="")
    if root.left.left.nextRight:
        print(root.left.left.nextRight.data)
    else:
        print(-1)