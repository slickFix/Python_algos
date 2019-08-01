class Node:

    def __init__(self,data):
        self.data = data
        self.next_node = None

class C_ll:

    def __init__(self):
        self.head = None

    def print_ll(self):

        curr = self.head

        while curr.next_node is not self.head:
            print(curr.data,end= ' ')

            curr = curr.next_node

        print(curr.data)

    def insert_sorted(self,data):

        new_node = Node(data)

        print(data)

        if self.head is None:
            self.head = new_node
            new_node.next_node = new_node
            return

        else:
            if self.head.next_node == self.head:
                if data > self.head.data:
                    self.head.next_node = new_node
                    new_node.next_node = self.head

                    return

                else:
                    new_node.next_node = self.head
                    self.head.next_node = new_node
                    self.head = new_node

                    return

            else:
                curr = self.head

                if data<curr.data:
                    new_node.next_node = self.head
                    curr = self.head

                    while curr.next_node is not self.head:
                        curr = curr.next_node

                    curr.next_node = new_node
                    self.head = new_node
                    return


                while curr.next_node != self.head:
                    if data>curr.data and data< curr.next_node.data:
                        new_node.next_node = curr.next_node
                        curr.next_node = new_node
                        return

                    else:
                        curr= curr.next_node


if __name__ == '__main__':

    c_ll = C_ll()

    for i in range(9,-1,-1):
        c_ll.insert_sorted(i)

    print('insert done')
    c_ll.print_ll()


