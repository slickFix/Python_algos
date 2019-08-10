def get_order(val):

    if val == '^':
        return 5
    elif val == '*' or val == '/':
        return 4
    elif val == '+' or val == '-':
        return 3
    else:
        return 1 # for case val = "("

def remove_till_open_paranthesis(stack):

    while True:

        if len(stack)>0 and stack[-1] != '(' :
            print(stack.pop(),end='')
        elif len(stack)>0 and stack[-1] == '(':
            stack.pop()
            return
        else:   # case where there was no '(' that means stack is empty now
            print('$$')
            return



if __name__ == '__main__':

    for i in range(int(input('Enter no of use cases : ').strip())):
        str = list(input("Enter the infix string : ").strip())

        stack = []

        # traversing the infix string
        for char in str:

            if char.isalpha():
                print(char,end='')

            elif char == '(':
                stack.append(char)

            elif char == ')':
                remove_till_open_paranthesis(stack)

            else:
                while len(stack) > 0 and get_order(char) <= get_order(stack[-1]):
                    print(stack.pop(), end='')

                stack.append(char)

        while len(stack) > 0:
            print(stack.pop(), end='')

        print()

''' Test use cases '''
# 2
# (a+b)*(c+d)
# (a-(b^c))+(d)