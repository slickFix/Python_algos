class Stack:

    def __init__(self):
        self.arr = []

    def push(self,data):

        self.arr.append(data)

        print(data,' item pushed to stack')

    def is_empty(self):

        if len(self.arr) == 0:
            return True
        else:
            return False

    def pop(self):

        if self.is_empty():
            print('Invalid operation as stack is empty')
            return

        return self.arr.pop()

    def peek(self):

        if self.is_empty():
            print('Invalid operation as stack is empty')
            return

        return self.arr[len(self.arr)-1]

if __name__ == '__main__':

    st = Stack()

    for i in range(10):
        st.push(i)

    for i in range(11):
        print(st.pop())