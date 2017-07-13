for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    maxi = -1
    for i in range(n-1, -1, -1):
        if arr[i]>maxi:
            maxi = arr[i]
        else:
            arr.pop(i)

    print(*arr, sep=" ")
