class Node:
    def __init__(self,data):
        self.data = data
        self.next_node = None

class C_ll:

    def __init__(self):
        self.last = None

    def print_ll(self):

        curr = self.last.next_node

        print(curr.data, end= ' ')

        curr = curr.next_node

        while curr !=self.last.next_node :

            print(curr.data, end= ' ')
            curr = curr.next_node

    def insert_f(self,data):

        new_node = Node(data)

        new_node.next_node = self.last.next_node

        self.last.next_node = new_node

    def insert_l(self,data):

        new_node = Node(data)

        new_node.next_node = self.last.next_node

        self.last.next_node = new_node

        self.last = new_node



if __name__ == '__main__':

    c_ll = C_ll()

    new_node = Node(10)
    new_node.next_node = new_node
    c_ll.last = new_node

    print('printing c_ll after 1st node is entered')

    c_ll.print_ll()

    print()

    print('Adding 1 to 9 nodes at the 1st position ')

    for i in range(9,0,-1):
        c_ll.insert_f(i)

    print('printing c_ll  after 1 to 9 nodes are added at first position')

    c_ll.print_ll()

    print()

    print('Adding 11 to 15 nodes at the last position  ')

    for i in range(11, 16):
        c_ll.insert_l(i)

    print('printing c_ll  after 11 to 15 nodes are added at last position')

    c_ll.print_ll()

