def reverse_stack(stack,rev_stack):

    if len(stack) == 0:
        return rev_stack

    top_element = stack.pop()
    rev_stack = rev_stack + [top_element]

    rev_stack = reverse_stack(stack,rev_stack)
    return  rev_stack

def _insert_at_bottom(stack,val):
    if len(stack) == 0 :
        return stack + [val]

    element = stack.pop()
    stack = _insert_at_bottom(stack,val)
    stack = stack + [element]
    return stack

def reverse_in_single_stack(stack):

    if len(stack)==0:
        return []

    top_element = stack.pop()
    rev_stack = reverse_in_single_stack(stack)
    rev_stack = _insert_at_bottom(rev_stack,top_element)

    return rev_stack



if __name__ == '__main__':

    n = int(input("Enter the no of elements in the stack : ").strip())

    stack = []

    for i in range(n):
        element = int(input().strip())
        stack.append(element)

    print('Printing the stack')
    print(stack)

    print()
    print('Reversing the stack')
    #rev_stack = reverse_stack(stack,[])
    rev_stack = reverse_in_single_stack(stack)

    print('Printing the reverse stack')
    print(rev_stack)
