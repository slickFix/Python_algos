class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Index:
    def __init__(self):
        self.data = 0

def search(inorder,st_inorder,en_inorder,data):

    for i in range(st_inorder,en_inorder+1):
        if inorder[i] == data:
            return i

def build_tree(index,inorder,preorder,st_inoder,en_inorder):
    if (st_inoder > en_inorder):
        return None

    node = Node(preorder[index.data])
    index.data += 1

    if (st_inoder == en_inorder):
        return  node

    in_index = search(inorder,st_inoder,en_inorder,node.data)

    node.left = build_tree(index,inorder,preorder,st_inoder,in_index-1)
    node.right = build_tree(index,inorder,preorder,in_index+1,en_inorder)

    return node


def printInorder(node):
    if node is None:
        return

    printInorder(node.left)

    print(node.data,end= ' ')

    printInorder(node.right)

if __name__ == '__main__':

    inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
    preOrder = ['A', 'B', 'D', 'E', 'C', 'F']

    index = Index()
    root = build_tree(index,inOrder, preOrder, 0, len(inOrder) - 1)

    # Let us test the build tree by priting Inorder traversal
    print("Inorder traversal of the constructed tree is")
    printInorder(root)