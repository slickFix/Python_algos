class Node:

    def __init__(self,data):

        self.data = data
        self.left = None
        self.right = None

def inorder_print(node):

    stack = []

    stack.append(node)

    while len(stack)>0:

        curr_node = stack[-1]

        if curr_node.left is not None:
            stack.append(curr_node.left)
            continue

        stack.pop()
        print(curr_node.data,end= ' ')

        if curr_node.right is not None:
            stack.append(curr_node.right)
        elif len(stack)>0:
            curr_node = stack.pop()
            print(curr_node.data,end=' ')

            if curr_node.right is not None:
                stack.append(curr_node.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.right = Node(6)
    root.left.left.right.left = Node(7)
    root.left.left.right.right = Node(8)
    inorder_print(root)