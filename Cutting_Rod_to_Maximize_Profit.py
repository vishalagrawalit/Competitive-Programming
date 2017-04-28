def profit(total, arr, values):
    n = len(arr)
    lis = [[0]*(total+1) for i in range(n)]

    for i in range(1, total+1):
        if arr[0] >= i and arr[0]%i==0:
            lis[0][i] = (i//arr[0])*values[0]

    for i in range(2,n+1):
        for j in range(1,total+1):
            if arr[i-1] >= j:
                lis[i][j-1] = max(lis[i-1][j-1] , lis[i][j-arr[i-1]-1] + values[i-1])
            else:
                lis[i][j-1] = lis[i-1][j-1]

    return lis[n-1][total]

arr = list(map(int,input().split()))
values = list(map(int,input().split()))
total = int(input())

print(profit(total, arr, values))
