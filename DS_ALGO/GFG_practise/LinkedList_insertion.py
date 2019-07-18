class Node:
    def __init__(self,data):

        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self,head_node):

        self.head = head_node

    def add_last(self,new_data):

        curr_node = self.head

        # moving to the tail node
        while curr_node.next_node is not None:
            curr_node = curr_node.next_node

        curr_node.next_node = Node(new_data)


    def add_first(self,new_data):

        # changing the reference of the head node

        new_node = Node(new_data)

        new_node.next_node = self.head

        self.head = new_node

    def add_after(self,data,new_data):

        # moving curr_node reference to the data node
        curr_node = self.head

        if curr_node.data == data:
            new_node = Node(new_data)
            new_node.next_node = curr_node.next_node

            curr_node.next_node = new_node

        else:
            while curr_node.next_node is not None:
                curr_node = curr_node.next_node

                if curr_node.data == data:
                    break

            if curr_node.next_node is None:
                # adding after last node

                curr_node.next_node = Node(new_data)

            else:
                new_node = Node(new_data)
                new_node.next_node = curr_node.next_node

                curr_node.next_node = new_node

    def print_nodes(self):

        curr_node = self.head

        while curr_node.next_node is not None:

            print(curr_node.data)

            curr_node = curr_node.next_node


if __name__ == '__main__':

    head_node = Node(0)
    ll = LinkedList(head_node)

    #checking add last
    for i in range(1,6):
        ll.add_last(i)

    ll.print_nodes()
    print()

    #checking add after
    ll.add_after(2,100)

    ll.print_nodes()

    print()

    #checking add first
    for i in range(6,15):
        ll.add_first(i)

    ll.print_nodes()
