class Queue_k:

    def __init__(self,k,n):

        self.k = k
        self.n = n
        self.arr = [None]*n
        self.next = [i for i in range(1, n+1)]
        self.front = [-1]*k
        self.rear = [-1]*k
        self.free = 0

    def is_empty(self,k):
        return self.front[k] == -1

    def is_full(self):
        return self.free == self.n

    def enque(self,data,k):

        if self.is_full():
            print('Array is full')
            return

        next_free = self.next[self.free]

        if self.is_empty(k):
            self.rear[k] = self.front[k] = self.free
        else:
            self.next[self.rear[k]] = self.free
            self.rear[k] = self.free

        self.next[self.free] = -1
        self.arr[self.free] = data

        self.free = next_free

    def deque(self,k):

        if self.is_empty(k):
            print('Array is empty')
            return

        indx = self.front[k]

        self.front[k] = self.next[indx]
        self.next[indx] = self.free
        self.free = indx

        return self.arr[indx]


if __name__ == '__main__':

    q_k = Queue_k(3,10)

    q_k.enque(15, 2)
    q_k.enque(45, 2)


    q_k.enque(17, 1)
    q_k.enque(49, 1)
    q_k.enque(39, 1)


    q_k.enque(11, 0)
    q_k.enque(9, 0)
    q_k.enque(7, 0)

    print("Dequeued element from queue 2 is " +
          str(q_k.deque(2)))
    print("Dequeued element from queue 1 is " +
                       str(q_k.deque(1)))
    print("Dequeued element from queue 0 is " +
                       str(q_k.deque(0)))