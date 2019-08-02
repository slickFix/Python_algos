class Node:

    def __init__(self,data):
        self.data  = data
        self.next_node = None
        self.prev_node = None

class Doubly_ll:

    def __init__(self):
        self.head = None

    def print_ll(self):

        curr = self.head

        while curr is not None:
            print(curr.data,end = ' ')
            curr = curr.next_node

    def insert_f(self,data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node

    def insert_l(self,data):

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


    def insert_pos(self,data,pos):
        ''' Assuming the position given will always be smaller than the length of LL
            1st position means after head
        '''

        new_node = Node(data)

        curr = self.head

        count = 0

        while count < pos-1:
            curr = curr.next_node
            count+=1

        new_node.next_node = curr.next_node
        curr.next_node.prev_node = new_node
        curr.next_node = new_node
        new_node.prev_node = curr

if __name__ == '__main__':

    d_ll = Doubly_ll()

    print('inserting nodes')

    for i in range(10):
        d_ll.insert_l(i)

    print('printing the doubly ll')

    d_ll.print_ll()