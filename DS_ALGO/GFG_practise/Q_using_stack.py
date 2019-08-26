class Queue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enque(self,data):

        while len(self.s1) != 0 :
            self.s2.append(self.s1.pop())

        self.s1.append(data)

        while len(self.s2) != 0 :
            self.s1.append(self.s2.pop())

    def deque(self):

        return self.s1.pop()

    def print_q(self):

        for i in range(len(self.s1)-1,-1,-1):
            print(self.s1[i],end=',')

        print()


# Driver code
if __name__ == '__main__':
    q = Queue()
    q.enque(1)
    q.enque(2)
    q.enque(3)

    q.print_q()
