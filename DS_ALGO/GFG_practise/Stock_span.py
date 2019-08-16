# code

# sample test case
# 1
# 7
# 100 80 60 70 60 75 85

# 1
# 134
# 74 665 742 512 254 469 748 445 663 758 38 60 724 142 330 779 317 636 591 243 289 507 241 143 65 249 247 606 691 330 371 151 607 702 394 349 430 624 85 755 357 641 167 177 332 709 145 440 627 124 738 739 119 483 530 542 34 716 640 59 305 331 378 707 474 787 222 746 525 673 671 230 378 374 298 513 787 491 362 237 756 768 456 375 32 53 151 351 142 125 367 231 708 592 408 138 258 288 554 784 546 110 210 159 222 189 23 147 307 231 414 369 101 592 363 56 611 760 425 538 749 84 396 42 403 351 692 437 575 621 597 22 149 800

'''
Approach similar to NGE

Also Stock span approach can be applied to NGE

'''

if __name__ == '__main__':

    for i in range(int(input().strip())):

        n = int(input().strip())

        arr = list(map(int, input().strip().split()))

        stack = []
        span = [None] * n
        stack.append(len(arr) - 1)

        for i in range(len(arr) - 1, -1, -1):

            stack_ind = stack.pop()
            element = arr[stack_ind]

            nge = arr[i]

            while nge > element:
                span_val = stack_ind - i
                span[stack_ind] = span_val

                if len(stack) > 0:
                    stack_ind = stack.pop()
                    element = arr[stack_ind]
                else:
                    break

            if nge <= element:
                stack.append(stack_ind)
                stack.append(i)

            else:
                stack.append(i)

        if len(stack) > 0:

            while len(stack) > 0:
                stack_ind = stack.pop()
                span[stack_ind] = stack_ind + 1

        for i in range(len(span)):
            print(span[i], end=' ')

        print()


