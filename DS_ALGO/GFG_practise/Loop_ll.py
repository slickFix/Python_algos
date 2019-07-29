class Node:

    def __init__(self,data):

        self.data =data
        self.next_node = None

class Linked_List:

    def __init__(self):
        self.head = None

    def print_ll(self):

        curr = self.head

        count  = 0
        while curr is not None and count < 16:

            print(curr.data, end=' ')

            curr = curr.next_node
            count += 1

    def detect_loop(self):

        curr = self.head

        bag = set()

        if curr is not None:
            bag.add(curr)
        else:
            return

        while curr.next_node is not None:

            if curr.next_node in bag:
                print('loop starts at ',curr.data)

                # loop removed
                curr.next_node = None
            else:
                bag.add(curr.next_node)
                curr = curr.next_node

    def push(self,data):

        curr = self.head

        new_node = Node(data)

        new_node.next_node = self.head

        self.head = new_node

if __name__ == '__main__':

    ll = Linked_List()

    tail = Node(10)

    ll.head = tail

    for i in range(9,-1,-1):
        ll.push(i)

    # creating loop

    tail.next_node = ll.head

    print('printing looped ll')
    ll.print_ll()

    print('detecting and removing loop')

    ll.detect_loop()

    print('printing ll after loop removal ')

    ll.print_ll()