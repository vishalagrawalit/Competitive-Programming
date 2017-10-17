for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    c = sum(arr)
    for i in range(min(k, n-k)):
        c -= 2*arr[i]
    print(c)
