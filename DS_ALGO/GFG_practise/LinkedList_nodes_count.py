class Node:

    def __init__(self,data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):

        self.head = None

    def add_last(self,data):

        curr_head = self.head

        # takes it to the last node
        while curr_head.next_node is not None:
            curr_head = curr_head.next_node

        new_node = Node(data)
        curr_head.next_node = new_node

    def count_node_iterative(self):

        curr_node = self.head

        if curr_node is None:
            print(0)
            return

        number = 0

        while curr_node.next_node is not None:
            number += 1
            curr_node = curr_node.next_node

        number += 1

        print(number)

    def count_node_recursive(self,head):

        if head is None:
            return 0

        return 1+ self.count_node_recursive(head.next_node)



if __name__ == '__main__':

    ll = LinkedList()
    ll.head = Node(0)

    for i in range(1,100):
        ll.add_last(i)

    ll.count_node_iterative()
    print(ll.count_node_recursive(ll.head))
