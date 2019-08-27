def tour(lis, n):
    # Code here

    start_in = 0
    curr_in = 0

    curr_petrol = lis[curr_in][0] - lis[curr_in][1]
    curr_in = (curr_in + 1) % n

    while True:

        if curr_petrol < 0:
            curr_petrol -= (lis[start_in][0] - lis[start_in][1])
            start_in += 1

            if start_in == n:
                return -1

            if start_in < curr_in:
                continue

            # adding the petrol to move to next location
            curr_petrol += (lis[curr_in][0] - lis[curr_in][1])

            # updating the curr_in
            curr_in = (curr_in + 1) % n

            continue

        # adding the petrol to move to next location
        curr_petrol += (lis[curr_in][0] - lis[curr_in][1])

        # updating the curr_in
        curr_in = (curr_in + 1) % n

        if curr_in == start_in and curr_petrol >= 0:
            return start_in

if __name__ == '__main__':

    for i in range(int(input())):
        n = int(input())
        arr = list(map(int,input().strip().split()))

        lis = []

        for i in range(1,2*n,2):
            lis.append([arr[i-1],arr[i]])

        print(tour(lis,n))

