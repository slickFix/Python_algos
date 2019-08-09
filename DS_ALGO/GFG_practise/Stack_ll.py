class Node:

    def __init__(self,data):
        self.data = data
        self.next_node = None

class Stack:

    def __init__(self):
        self.tail  = None

    def is_empty(self):

        if self.tail is None :
            return True
        else:
            return False


    def peek(self):

        print('last node is ',self.tail)
        return  self.tail

    def print_stack(self):

        curr = self.tail

        while curr is not None:
            print(curr.data,' -> ',end=' ')
            curr = curr.next_node

        print()

    def push(self,data):

        new_node = Node(data)

        if self.tail is None :
            self.tail = new_node

        else:
            new_node.next_node = self.tail
            self.tail = new_node

    def pop(self):

        if self.is_empty():
            print('Pop operation is not possible as stack is empty')
            return

        else:
            ret_data = self.tail.data
            prev_node = self.tail.next_node
            self.tail.next_node = None
            self.tail = prev_node

            print(ret_data,' item popped.')

            return

if __name__ == '__main__':

    st = Stack()
    for i in range(10):
        st.push(i)

    print('Printing stack.')
    st.print_stack()


    for i in range(11):
        st.pop()