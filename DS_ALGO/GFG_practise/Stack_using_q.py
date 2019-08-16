from queue import Queue


# push operation is costly
class Stack:

    def __init__(self):

        self.q1 = Queue()
        self.q2 = Queue()

    def push(self,data):

        self.q2.put(data)

        while not self.q1.empty():
            self.q2.put(self.q1.get())

        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q

    def pop(self):

        if self.q1.empty():
            return "stack is empty"
        else:
            return self.q1.get()


if __name__ == '__main__':

    s = Stack()

    for i in range(10):
        s.push(i)


    for i in range(12):
        print(s.pop())