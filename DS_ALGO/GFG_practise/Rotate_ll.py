class Node:
    def __init__(self,data):

        self.data = data
        self.next_node = None

class Linked_List:

    def __int__(self):
        self.head = None

    def print_ll(self):

        curr= self.head

        while curr is not None:

            print(curr.data,end= ' ')
            curr = curr.next_node

    def rotate(self,k):

        curr = self.head

        while curr.next_node is not None:

            curr = curr.next_node

        curr.next_node = self.head

        curr= self.head

        for i in range(1,k):
            curr= curr.next_node

        self.head  = curr.next_node
        curr.next_node =None




    def push(self,data):

        new_node = Node(data)

        new_node.next_node = self.head

        self.head = new_node


if __name__ ==  '__main__':

    ll  = Linked_List()

    head = Node(10)

    ll.head = head


    for i in range(9,-1,-1):
        ll.push(i)

    print('printing the list of nodes ')

    ll.print_ll()

    print()
    print('rotating the nodes by 3')

    ll.rotate(3)

    print()

    print('printing the rotated list ')

    ll.print_ll()