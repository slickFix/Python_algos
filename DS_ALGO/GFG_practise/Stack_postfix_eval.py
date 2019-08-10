
# Sample test case
# 2
# 231*+9-
# 123+*8-
# Sample test case answers
# -4
# -3


''' Strategy - if "digit" put it in stack else pop 2 numbers and apply operation and push the resultant in stack'''

if __name__ == '__main__':
    for i in range(int(input().strip())):

        exp = list(input().strip())

        stack = []

        for ch in exp:

            if ch.isdigit():
                stack.append(int(ch))

            else:
                no1 = stack.pop()
                no2 = stack.pop()

                if ch == '*':
                    result = no1 * no2
                if ch == '/':
                    result = no2 // no1
                if ch == '-':
                    result = no2 - no1
                if ch == '+':
                    result = no1 + no2

                stack.append(result)

        print(stack.pop())