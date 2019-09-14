class Node:
    def __init__(self,data):
        self.key = data
        self.left = self.right = None


def find_pre(root):
    curr = root

    while curr.right is not None:
        curr = curr.right

    return curr

def find_suc(root):
    curr = root

    while curr.left is not None:
        curr = curr.left

    return curr

def findPreSuc(root,key):

    if root is None:
        return

    if root.key == key:

        if root.left is not None and root.right is not None:
            findPreSuc.pre = find_pre(root.left).key
            findPreSuc.suc = find_suc(root.right).key

        elif root.right is None and root.left is None:
            return

        elif root.right is None:
            findPreSuc.pre = find_pre(root.left).key

        else:
            findPreSuc.suc = find_suc(root.right).key

    else:

        if key > root.key:
            findPreSuc.pre = root.key
            findPreSuc(root.right,key)

        else :
            findPreSuc.suc = root.key
            findPreSuc(root.left,key)


def insert(root,data):

    if root is None:
        return Node(data)

    if data > root.key:
        root.right  = insert(root.right,data)

    elif data < root.key:
        root.left  = insert(root.left,data)

    else:
        return root

    return root

if __name__ == '__main__':

    key = 65  # Key to be searched in BST

    """ Let us create following BST 
                  50 
               /     \ 
              30      70 
             /  \    /  \ 
           20   40  60   80  
    """
    root = None
    root = insert(root, 50)
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);

    # Static variables of the function findPreSuc
    findPreSuc.pre = None
    findPreSuc.suc = None

    findPreSuc(root, key)

    if findPreSuc.pre is not None:
        print("Predecessor is", findPreSuc.pre)

    else:
        print("No Predecessor")

    if findPreSuc.suc is not None:
        print("Successor is", findPreSuc.suc)
    else:
        print("No Successor")
