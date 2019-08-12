
# test use case
# 11 13 21 3
# [34, 85, 18, 27, 54, 93, 66, 72, 30, 67]

# result
'''
11's NGE is 13
13's NGE is 21
3's NGE is -1
'''


import random

if __name__ == '__main__':

    # arr = list(map(int,input().strip().split()))

    arr = []

    for i in range(10):
        arr.append(random.randint(1,100))

    print(arr)

    stack = []

    stack.append(arr[0])

    for i in range(1,len(arr)):

        stack_top_element = stack.pop()

        next_element = arr[i]

        while stack_top_element < next_element:
            print("{}'s NGE is {}".format(stack_top_element,next_element))

            if len(stack) > 0:
                stack_top_element  = stack.pop()
            else:
                break

        if stack_top_element > next_element:
            stack.append(stack_top_element)
            stack.append(next_element)

        else:
            stack.append(next_element)

    if len(stack)>0:

        while len(stack)>0:
            element = stack.pop()
            print("{}'s NGE is {}".format(element,-1))



