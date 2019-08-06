class Node :

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
            print(curr.data,end=' ')

            curr = curr.next_node

    def add_node_l(self,data):

        new_node = Node(data)

        curr = self.head

        # head is None
        if curr is None:
            self.head = new_node
            return

        while curr.next_node is not None:
            curr = curr.next_node

        curr.next_node = new_node
        new_node.prev_node = curr



    def delete_node(self,pos):

        curr = self.head

        if pos == 1:
            curr.data = curr.next_node.data
            x = 2

        count = 1

        while count != pos - 1:
            curr = curr.next_node
            count += 1

        if curr.next_node.next_node is not None:
            del_node = curr.next_node

            curr.next_node = del_node.next_node
            del_node.next_node = None

            curr.next_node.prev_node = curr
            del_node.prev_node = None

        else:
            curr.next_node.prev_node = None
            curr.next_node = None



if __name__ == '__main__':

    d_ll = Doubly_ll()

    print("Adding nodes 0 to 10")

    for i in range(11):
        d_ll.add_node_l(i)

    print('Printing LL ')
    d_ll.print_ll()

    print()
    print('Deleting node at position 3')
    d_ll.delete_node(3)

    print("Printing nodes after delete operation ")
    d_ll.print_ll()