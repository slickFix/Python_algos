from collections import deque


def print_max(arr,n,k):

    q = deque()

    for i in range(k):


        while q and arr[i] >= arr[q[-1]]:
            q.pop()

        q.append(i)

    for i in range(k,n):


        print(arr[q[0]],end=',')

        while q and q[0]<=i-k:
            q.popleft()

        while q and arr[i] >= arr[q[-1]]:
            q.pop()

        q.append(i)

    print(arr[q[0]])


if __name__=="__main__":
    arr = [12, 1, 78, 90, 57, 89, 56]
    k = 3
    print_max(arr, len(arr), k)