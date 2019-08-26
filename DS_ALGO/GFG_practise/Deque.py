class Deque:

    def __init__(self,capacity):

        self.capacity = capacity
        self.arr = [None]*capacity
        self.size = self.front = 0
        self.rear = capacity-1

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enque_f(self,data):

        if self.is_full():
            print('Q is full')
            return

        self.front = (self.front -1) % self.capacity
        self.arr[self.front] = data
        self.size +=1

    def enque_l(self,data):

        if self.is_full():
            print('Q is full')
            return

        self.rear = (self.rear + 1) % (self.capacity)
        self.arr[self.rear] = data
        self.size = self.size + 1

    def deque_f(self):

        if self.is_empty():
            print('Q is empty')
            return

        data = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

    def deque_l(self):

        if self.is_empty():
            print('Q is empty')
            return

        data = self.arr[self.rear]
        self.rear = (self.rear - 1) % self.capacity
        self.size -=1

        return data

    def print_q(self):

        front = self.front
        rear = self.rear

        if abs(self.front -self.rear) == 1:

            while front != rear:
                print(self.arr[front], end=',')
                front = (front + 1) % self.capacity

            print(self.arr[rear])

        else:

            rear = (self.rear + 1) % self.capacity
            while front != rear:
                print(self.arr[front], end=',')
                front = (front + 1) % self.capacity

            print(self.arr[rear])



# Driver Code
if __name__ == '__main__':
    queue = Deque(3)
    queue.enque_f(10)
    queue.enque_f(20)
    queue.enque_l(30)

    print('first')
    queue.print_q()


    queue.enque_l(40)
    queue.deque_f()
    queue.enque_l(50)

    print('second')
    queue.print_q()


