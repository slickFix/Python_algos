
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


def getMaxWidth(root):

    q = []

    q.append((root, 1))

    max_w = 0
    prev_ht = 0
    curr_w = 0

    while len(q) != 0:

        node, ht = q.pop(0)

        if node.left is not None:
            q.append((node.left, ht + 1))
        if node.right is not None:
            q.append((node.right, ht + 1))

        if ht != prev_ht:

            if curr_w > max_w:
                max_w = curr_w
            curr_w = 1
            prev_ht = ht

        else:
            curr_w += 1

        if curr_w > max_w:
            max_w = curr_w

    return max_w

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)

    print("Maximum width is %d" % (getMaxWidth(root)))