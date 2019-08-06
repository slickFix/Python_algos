class Node:

    def __init__(self,data):

        self.data = data
        self.next_node = None
        self.prev_node = None

class Doubly_ll:

    def __init__(self):
        self.head = None

    def print_ll(self):

        curr = self.head

        while curr.next_node is not None:
            print(curr.data, end = ' ')

            curr = curr.next_node

    def insert_l(self,data):

        new_node = Node(data)

        curr  = self.head

        if self.head is None:
            self.head = new_node

        else:

            while curr.next_node is not None:
                curr = curr.next_node

            curr.next_node = new_node
            new_node.prev_node = curr

    def reverse_d_ll(self):

        curr = self.head

        while curr.next_node is not  None:
            temp = curr.next_node

            curr.next_node = curr.prev_node
            curr.prev_node = temp

            if curr.next_node is not None:
                self.head = curr

            curr = curr.prev_node





if __name__ == '__main__':

    print('Adding nodes 0 to 10')

    d_ll = Doubly_ll()

    for i in range(11):
        d_ll.insert_l(i)


    print('Printing d_ll')

    d_ll.print_ll()

    print()
    print('Reversing the d_ll')

    d_ll.reverse_d_ll()

    print('Printing d_ll reversed')

    d_ll.print_ll()