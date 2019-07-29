class Node:

    def __init__(self,data):

        self.data = data
        self.next_node = None

class Linked_List:

    def __init__(self):
        self.head = None


    def print_ll(self):

        curr = self.head

        while curr is not None:
            print(curr.data, end= ' ')
            curr = curr.next_node

        print()


    def push(self,data):

        curr = self.head

        new_node = Node(data)

        new_node.next_node = curr

        self.head = new_node

    def reverse_k(self,head,k):

        curr = head
        prev = None
        next_n = curr
        count = 0

        while (curr is not None and count < k):

            next_n = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = next_n
            count+=1

        if next_n is not None:
            head.next_node = self.reverse_k(next_n,k)

        return prev

if __name__ == '__main__':

    ll = Linked_List()

    f_node = Node(10)

    ll.head = f_node

    for i in range(9,-1,-1):
        ll.push(i)

    print('printing ll before reverse_k is called')

    ll.print_ll()

    print('reversing list ')

    ll.head = ll.reverse_k(ll.head,3)

    ll.print_ll()


