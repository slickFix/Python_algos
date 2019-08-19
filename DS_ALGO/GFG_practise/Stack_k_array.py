class Kstack:

    def __init__(self,k,n):

        self.k = k
        self.n = n

        self.arr = [0]*n
        self.top = [-1]*k
        self.next = [i for i in range(1,n+1)]

        self.free = 0

    def is_full(self):

        return self.free == self.n

    def is_empty(self,stack_n):

        return self.top[stack_n] == -1

    def push(self,data,stack_n):

        if  self.is_full():
            print('Stack overflow')
            return

        insert_at = self.free
        self.free = self.next[self.free]
        self.arr[insert_at] = data
        self.next[insert_at] = self.top[stack_n]
        self.top[stack_n] = insert_at

    def pop(self,stack_n):

        if self.is_empty(stack_n):
            print('Stack is empty')
            return

        top_index = self.top[stack_n]
        self.top[stack_n] = self.next[top_index]
        self.next[top_index] = self.free
        self.free = top_index

        return self.arr[top_index]

    def printstack(self,stack_n):

        if self.is_empty(stack_n):
            print('Stack is empty')
            return

        top_index = self.top[stack_n]

        while top_index != -1:
            print(self.arr[top_index],end = ' ')
            top_index = self.next[top_index]

        print()

if __name__ == '__main__':

    # Create 3 stacks using an
    # array of size 10.
    kstacks = Kstack(3, 10)

    # Push some items onto stack number 2.
    kstacks.push(15, 2)
    kstacks.push(45, 2)

    # Push some items onto stack number 1.
    kstacks.push(17, 1)
    kstacks.push(49, 1)
    kstacks.push(39, 1)

    # Push some items onto stack number 0.
    kstacks.push(11, 0)
    kstacks.push(9, 0)
    kstacks.push(7, 0)

    print("Popped element from stack 2 is " +
          str(kstacks.pop(2)))
    print("Popped element from stack 1 is " +
          str(kstacks.pop(1)))
    print("Popped element from stack 0 is " +
          str(kstacks.pop(0)))

    kstacks.printstack(0)





