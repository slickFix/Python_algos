class Queue:

    def __init__(self,capacity):

        self.capacity = capacity
        self.Q = [None]* capacity

        self.rear = capacity-1
        self.front = self.size = 0

    def is_full(self):

        return self.size == self.capacity

    def is_empty(self):

        return self.size == 0

    def enque(self,data):

        if self.is_full():
            print('Queue is full')
            return

        self.rear = (self.rear+1) % (self.capacity)
        self.Q[self.rear] = data
        self.size = self.size +1

    def deque(self):

        if self.is_empty():
            print("Queue is empty")
            return

        data = self.Q[self.front]
        self.front = (self.front +1) % self.capacity
        self.size -=1

        return data

    def que_front(self):
        if self.is_empty():
            print("Queue is empty")

        print("Front item is", self.Q[self.front])


    def que_rear(self):
        if self.is_empty():
            print("Queue is empty")
        print("Rear item is", self.Q[self.rear])


# Driver Code
if __name__ == '__main__':
    queue = Queue(30)
    queue.enque(10)
    queue.enque(20)
    queue.enque(30)
    queue.enque(40)
    queue.deque()
    queue.que_front()
    queue.que_rear()