

# Input:
# 1
# 5
# 20 8 4 22 12
# 3
# Output:
# 12

class Node:
    def __init__(self,data,key):
        self.key = key
        self.data = data
        self.right = self.left = None

def insert_node(root,node):
    ptraverse = root
    curparent = root

    while(ptraverse != None):
        curparent = ptraverse
        if node.data < ptraverse.data:
            ptraverse.key += 1
            ptraverse = ptraverse.left

        else:
            ptraverse = ptraverse.right

    if root is None:
        root = node
    elif node.data < curparent.data:
        curparent.left = node
    else:
        curparent.right = node

    return root

def build_bst(root,arr,n):
    for it in range(n):
        root = insert_node(root,Node(arr[it],0))

    return root


class It:
    def __init__(self):
        self.counter = 0


def k_smallest_element(root, n):
    # Code here
    it = It()

    return k_small(root, n, it).data


def k_small(root, n, it):
    if root is None:
        return None

    ret = k_small(root.left, n, it)

    if it.counter == n:
        return ret

    it.counter += 1

    if it.counter == n:
        return root

    ret = k_small(root.right, n, it)

    return ret

def print_inorder(root):
    if root is not None:
        print_inorder(root.left)
        print(root.data,end=' ')
        print_inorder(root.right)

if __name__ == '__main__':

    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        root = None

        root = build_bst(root,arr,n)
        k = int(input())
        print_inorder(root)
        print()
        print(k_smallest_element(root,k))