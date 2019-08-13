
### Pass by reference

def _ins_sort(ss, element):
    if len(ss) == 0:
        ss.append(element)
        return

    if element < ss[-1]:
        ss.append(element)

    else:
        pop_element = ss.pop()
        _insert_sort(ss, element)
        ss.append(pop_element)


def sorted(s):
    # Code here

    if len(s) == 0:
        return

    pop_element = s.pop()

    sorted(s)
    _insert_sort(s, pop_element)


# pass by value

def _insert_sort(sort_stack,element):

    if len(sort_stack) == 0:
        return sort_stack + [element]

    # increasing order stack sort
    if element > sort_stack[-1]:
        sort_stack = sort_stack+[element]
        return sort_stack

    else:
        pop_element = sort_stack.pop()
        sort_stack = _insert_sort(sort_stack,element)
        sort_stack = sort_stack +[pop_element]

        return  sort_stack


def sort(stack):

    if len(stack) == 0:
        return []

    element = stack.pop()
    sort_stack = sort(stack)
    sort_stack = _insert_sort(sort_stack,element)

    return sort_stack


if __name__ == '__main__':

    n = int(input("Enter the no of elements : ").strip())

    stack = []
    for i in range(n):
        element = int(input().strip())
        stack.append(element)


    print("Printing the stack elements")
    print(stack)

    print("Sorting the stack")
    sort_stack = sort(stack)

    print()
    print("Printing the sorted stack elements")
    print(sort_stack)

