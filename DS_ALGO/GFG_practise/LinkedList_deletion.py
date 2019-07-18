class Node:

    def __init__(self,data):

        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.head = None

    def print_nodes(self):

        curr_node = self.head

        while curr_node is not None:

            print(curr_node.data,end=' ')

            curr_node = curr_node.next_node

    def insert_last(self,data):

        curr_node = self.head

        # reaching to the last node

        while curr_node.next_node is not None:
            curr_node = curr_node.next_node

        new_node = Node(data)

        curr_node.next_node = new_node

    def delete_node_data(self,data):

        curr_node = self.head

        if curr_node.data == data:

            self.head = curr_node.next_node
            return

        else:

            while curr_node.next_node is not None:

                if curr_node.next_node.data == data:
                    curr_node.next_node = curr_node.next_node.next_node

                else:
                    curr_node = curr_node.next_node

if __name__ == '__main__':

    ll = LinkedList()
    ll.head = Node(0)

    for i in range(1,10):
        ll.insert_last(i)

    ll.print_nodes()

    ll.delete_node_data(5)

    print()

    ll.print_nodes()

    ll.delete_node_data(9)

    print()

    ll.print_nodes()

    ll.delete_node_data(0)

    print()

    ll.print_nodes()

