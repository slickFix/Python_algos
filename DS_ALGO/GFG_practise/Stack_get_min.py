class Stack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self,data):

        self.stack.append(data)



        if len(self.min_stack) == 0:
            self.min_stack.append(data)

        elif self.min_stack[-1] > data:
            self.min_stack.append(data)

    def pop(self):

        element = self.stack.pop()

        if element == self.min_stack[-1]:
            self.min_stack.pop()

        return element

    def get_min(self):

        return self.min_stack[-1]

    def is_empty(self):

        if len(self.stack) == 0 :
            return True

        else:
            return False


if __name__ == '__main__':

    st = Stack()

    for i in range(10):
        st.push(i)

    print(st.get_min())

    for i in range(-1,-3,-1):
        st.push(i)

    print(st.get_min())


    for i in range(2):
        st.pop()

    print(st.get_min())