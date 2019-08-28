import queue

for i in range(int(input().strip())):

    n = int(input().strip())

    q = queue.Queue()

    q.put('1')
    print('1', end=' ')

    count = n - 1

    while count > 0:

        no = q.get()

        next_no = no + '0'
        q.put(next_no)

        print(next_no, end=' ')

        count -= 1

        if count == 0:
            break

        next_next_no = no + '1'
        q.put(next_next_no)

        print(next_next_no, end=' ')

        count -= 1

    print()