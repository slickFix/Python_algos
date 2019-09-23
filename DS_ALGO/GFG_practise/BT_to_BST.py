class Node:
    def __init__(self,data):

        self.data = data
        self.left = self.right = None

def storeInorder(root,inorder):

    # Base Case
    if root is None:
        return

    # First store the left subtree
    storeInorder(root.left, inorder)

    # Copy the root's data
    inorder.append(root.data)

    # Finally store the right subtree
    storeInorder(root.right, inorder)


# A helper funtion to count nodes in a binary tree
def countNodes(root):
    if root is None:
        return 0

    return countNodes(root.left) + countNodes(root.right) + 1


# Helper function that copies contents of sorted array
# to Binary tree
def arrayToBST(arr, root):
    # Base Case
    if root is None:
        return

        # First update the left subtree
    arrayToBST(arr, root.left)

    # now update root's data delete the value from array
    root.data = arr[0]
    arr.pop(0)

    # Finally update the right subtree
    arrayToBST(arr, root.right)


def binaryTreeToBST(root):
    # Base Case: Tree is empty
    if root is None:
        return

        # Count the number of nodes in Binary Tree so that
    # we know the size of temporary array to be created
    n = countNodes(root)

    # Create the temp array and store the inorder traveral
    # of tree
    arr = []
    storeInorder(root, arr)

    # Sort the array
    arr.sort()

    # copy array elements back to binary tree
    arrayToBST(arr, root)


# Print the inorder traversal of the tree
def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.data,)
    printInorder(root.right)

if __name__ == '__main__':


    # Driver program to test above function
    root = Node(10)
    root.left = Node(30)
    root.right = Node(15)
    root.left.left = Node(20)
    root.right.right = Node(5)

    # Convert binary tree to BST
    binaryTreeToBST(root)

    print("Following is the inorder traversal of the converted BST")
    printInorder(root)
