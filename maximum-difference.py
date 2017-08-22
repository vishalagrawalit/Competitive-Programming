for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    mini,maxi = 10**9, -1

    for i in range(n):
        if arr[i]-mini > maxi:
            maxi = arr[i]-mini
        else:
            mini = min(arr[i], mini)

    print(maxi)
            
