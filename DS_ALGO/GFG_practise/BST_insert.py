class Node:
    def __init__(self,data):
        self.data = data
        self.right = self.left = None


def insertinBST(root, node):
    # Code here

    if root.data < node.data:
        if root.right is not None:
            insertinBST(root.right, node)
        else:
            root.right = node

    else:
        if root.data == node.data:
            return

        elif root.left is not None:
            insertinBST(root.left, node)
        else:
            root.left = node


def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data,end=' ')
        traverseInorder(root.right)

'''
test case:
3
7
2 81 87 42 66 90 45 
4
6 7 9 8
4
1 1 2 1

output:
2 42 45 66 81 87 90
6 7 8 9
1 2
'''
if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        root = None
        for j in arr:
            if root is None:
                root = Node(j)
            else:
                insertinBST(root,Node(j))

        traverseInorder(root)
        print()