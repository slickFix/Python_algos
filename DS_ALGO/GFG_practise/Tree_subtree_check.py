class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def check_identical(root1,root2):

    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    return ((root1.data == root2.data) and check_identical(root1.left,root2.left) and check_identical(root1.right,root2.right))


# check if root2 tree is subtree of root1 tree
def check_subtree(root1,root2):
    if root1 is None:
        return False
    if root2 is None:
        return True

    if check_identical(root1, root2):
        return True

    return check_subtree(root1.left,root2) or check_subtree(root1.right,root2)

if __name__ == '__main__':
    """ TREE 1 
         Construct the following tree 
                  26 
                /   \ 
              10     3 
            /    \     \ 
          4      6      3 
           \ 
            30 
        """

    T = Node(26)
    T.right = Node(3)
    T.right.right = Node(3)
    T.left = Node(10)
    T.left.left = Node(4)
    T.left.left.right = Node(30)
    T.left.right = Node(6)

    """ TREE 2 
         Construct the following tree 
              10 
            /    \ 
          4      6 
           \ 
            30 
        """
    S = Node(10)
    S.right = Node(6)
    S.left = Node(4)
    S.left.right = Node(30)

    if check_subtree(T, S):
        print("Tree 2 is subtree of Tree 1")
    else:
        print("Tree 2 is not a subtree of Tree 1")
