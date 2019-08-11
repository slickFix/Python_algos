class Stack:

    def __init__(self,n):
        self.stack = [None]*n
        self.top1 = -1
        self.top2 = n

    def push1(self,data):

        self.top1+=1
        self.stack[self.top1] = data

    def push2(self,data):

        self.top2-=1

        self.stack[self.top2] = data

    def pop1(self):

        ret_data = self.stack[self.top1]
        self.top1 -=1
        return ret_data

    def pop2(self):

        ret_data = self.stack[self.top2]
        self.top2+=1

        return ret_data

    def peek1(self):
        return self.stack[self.top1]

    def peek2(self):
        return self.stack[self.top2]

    def print_stack(self):

        print(self.top1,self.top2,sep=' <-> ')

        for i in self.stack:
            print(i,end=' ')
        print()

if __name__ == '__main__':

    stack = Stack(20)

    print('Adding values 1 to 15 in stack1')
    for i in range(1,16):
        stack.push1(i)

    print('Printing the status of the stack')
    stack.print_stack()

    print('Adding values 20 to 17 in stack2')
    for i in range(20,16,-1):
        stack.push2(i)

    print('Printing the status of the stack')
    stack.print_stack()



