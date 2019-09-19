
# Example:
# Input:
# 2
# 7
# 20 8 22 4 12 10 14
# 8
# 7
# 20 8 22 4 12 10 14
# 10
# Output:
# 10
# 12

class Node:
    def __init__(self,data):
        self.data = data
        self.right = self.left = None

def insert(root,node):

    if root is None:
        return node

    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)
        elif root.data == node.data:
            return

        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left,node)

def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data ,end=' ')
        traverseInorder(root.right)


def minVal(root):
    curr = root

    while curr.left is not None:
        curr = curr.left

    return curr


def inorderSuccessor(root, X):
    # Code here

    curr = root
    retSuc = None

    while True:

        if curr.data > X.data:
            retSuc = curr
            curr = curr.left

        elif curr.data < X.data:
            curr = curr.right

        else:
            break

    if curr.right is not None:
        return minVal(curr.right)

    else:
        return retSuc

if __name__ == '__main__':

    for i in range(int(input().strip())):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        root = None

        for j in arr:
            if root is None:
                root = Node(j)
            else:
                insert(root,Node(j))

        k = int(input())
        ptr = inorderSuccessor(root,Node(k))

        if ptr  is None:
            print(-1)
        else:
            print(ptr.data)
