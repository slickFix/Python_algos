class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = None


class Linked_list:
    '''
    Assuming this class will be called either after the 1st node object is created and passed:

    Linked_list(1st_node,1st_node)

    OR

    Linked_list()

    '''

    def __init__(self, head_node=None, tail_node=None):
        self.head = head_node
        self.tail = tail_node
        if head_node is None and tail_node is None:
            self.number_nodes = 0
        elif head_node is not None and tail_node is not None:
            self.number_nodes = 1

    def print_list(self):

        curr_head = self.head

        index = 1
        while curr_head:
            print('Value at position ', index, ' : ', curr_head.data)
            curr_head = curr_head.next_node
            index += 1

    def add_node(self, new_node):

        # 1st node added
        if self.head is None and self.tail is None and self.number_nodes == 0:
            self.head = new_node
            self.tail = new_node
            self.number_nodes += 1

        # new nodes being added
        if self.tail is not None:
            self.tail.next_node = new_node
            self.tail = new_node
            self.number_nodes += 1


ll = Linked_list()
node1 = Node(4)
ll.add_node(node1)
for i in range(4):
    ll.add_node(Node(i))

ll.print_list()
