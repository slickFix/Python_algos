# code

for i in range(int(input().strip())):

    exp = list(input().strip())

    stack = []
    printed = False

    for char in exp:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)

        elif char == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                print('not balanced')
                printed = True
                break

        elif char == '}':
            if len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            else:
                print('not balanced')
                printed = True
                break

        elif char == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                print('not balanced')
                printed = True
                break

    if not printed:
        if len(stack) > 0:
            print('not balanced')

        else:
            print('balanced')

