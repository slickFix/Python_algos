import random

class Node:

    def __init__(self,data):

        self.data = data
        self.next_node = None
        self.prev_node = None

class Doubly_ll:

    def __init__(self):
        self.head = None

    def insert_l(self,data):

        new_node = Node(data)

        curr = self.head

        if curr is None:

            self.head = new_node
            return

        else:

            while curr.next_node is not None:
                curr = curr.next_node

            curr.next_node = new_node
            new_node.prev_node = curr

    def print_ll_pos(self,first_node):

        curr = first_node

        while curr is not None:

            print(curr.data, end= ' ')
            curr = curr.next_node

        print()

    def print_ll(self):

        curr = self.head

        while curr is not None:

            print(curr.data, end= ' ')
            curr = curr.next_node

        print()

    def _length_nodes(self,pointer):

        #print('head lenght pointer ',pointer.data)

        count = 0

        while pointer is not None:
            #print(pointer.data,end=' ')
            count+= 1
            pointer = pointer.next_node

        #print()

        return count

    def _get_left_right_head_nodes(self,first_node,length):

        curr = first_node

        count = 0

        while count != length-1:
            curr = curr.next_node
            count +=1

        right_head = curr.next_node

        curr.next_node = None
        right_head.prev_node = None

        return first_node,right_head

    def _merge_ll(self,left_head,right_head):

        left_pointer = left_head
        right_pointer = right_head

        if left_pointer.data < right_pointer.data:
            ret_head = left_pointer
        else:
            ret_head = right_pointer

        while left_pointer is not None and right_pointer is not None:
            if left_pointer.data < right_pointer.data:

                if left_pointer.next_node:

                    if left_pointer.next_node.data <= right_pointer.data:
                        left_pointer = left_pointer.next_node
                    else:
                        temp = left_pointer.next_node
                        left_pointer.next_node = right_pointer
                        right_pointer.prev_node = left_pointer
                        left_pointer = temp
                        continue

                else:
                    temp = left_pointer.next_node
                    left_pointer.next_node = right_pointer
                    right_pointer.prev_node = left_pointer
                    left_pointer = temp
                    continue
            else:

                if right_pointer.next_node:

                    if right_pointer.next_node.data <= left_pointer.data:
                        right_pointer = right_pointer.next_node

                    else:
                        temp = right_pointer.next_node
                        right_pointer.next_node = left_pointer
                        left_pointer.prev_node = right_pointer

                        right_pointer = temp
                        continue

                else:
                    temp = right_pointer.next_node
                    right_pointer.next_node = left_pointer
                    left_pointer.prev_node = right_pointer

                    right_pointer = temp
                    continue


        # self.print_ll_pos(ret_head)
        return ret_head


    def merge_sort_ll(self,first_node):

        length = self._length_nodes(first_node)

        if length == 1:
            return first_node

        if length >1:
            left_head,right_head = self._get_left_right_head_nodes(first_node,length//2)
            sorted_left = self.merge_sort_ll(left_head)
            sorted_right = self.merge_sort_ll(right_head)

            # print('left')
            # self.print_ll_pos(sorted_left)
            # print('right')
            # self.print_ll_pos(sorted_right)

            return self._merge_ll(sorted_left,sorted_right)


if __name__ == '__main__':

    d_ll = Doubly_ll()

    print('inserting random order node (10 nodes) ')

    for i in range(10):

        data = random.randint(10,99)

        d_ll.insert_l(data)

    # for i in [44,62,34,47,71,56,18,62,56,26]:
    #     data = random.randint(0, 100)
    #
    #     d_ll.insert_l(i)

    print('printing the nodes which are added randomly')

    d_ll.print_ll()

    # print(d_ll._length_nodes(d_ll.head))

    print('merge sorting the d_ll')
    d_ll.head = d_ll.merge_sort_ll(d_ll.head)

    print('printing the merge sorted d_ll')
    d_ll.print_ll()