class Node:
    def __init__(self,data):

        self.data = data
        self.next_node = None

class C_ll:

    def __init__(self):
        self.last = None

    def insert_f(self,data):

        if self.last is None:
            new_node = Node(data)
            self.last = new_node
            new_node.next_node = new_node

            return

        new_node = Node(data)
        new_node.next_node = self.last.next_node
        self.last.next_node = new_node

    def print_ll(self,head):

        curr = head

        print(curr.data,end = ' ')

        curr = curr.next_node

        while curr != head:
            print(curr.data,end= ' ')

            curr = curr.next_node

    def split_ll(self):

        head1 = self.last.next_node
        head2 = self.last.next_node


        while True:

            head1 = head1.next_node

            if head2.next_node is not None:
                head2 = head2.next_node.next_node
            else:
                break

            if head2.next_node != self.last.next_node and head2.next_node.next_node != self.last.next_node:
                pass
            else:
                break

        if head2.next_node is not None:
            head2 = head2.next_node

        return head1,head2

if __name__ == '__main__':

    c_ll = C_ll()

    print('Enter input : ')
    case = int(input())

    if case == 1:
        print('Adding nodes 1 to 9')

        for i in range(9,-1,-1):
            c_ll.insert_f(i)

        print('printing the list of node in c_ll ')

        print()
        c_ll.print_ll(c_ll.last.next_node)


        print('Doing the c_ll splits ')

        head1,head2 = c_ll.split_ll()

        print(head1.data,head2.data)

    if case == 2:
        print('Adding node 9')
        c_ll.insert_f(9)
        c_ll.insert_f(8)

        print('printing the list of nodes in c_ll')

        print()

        c_ll.print_ll(c_ll.last.next_node)

        head1,head2 = c_ll.split_ll()

        print()

        print(head1.data, head2.data)


