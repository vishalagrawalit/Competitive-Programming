def ways_of_coins(arr, total, n):
    
    lis = [[0]*(total+1) for i in range(n)]

    for i in range(n):
        lis[i][0]=1
        
    for i in range(n):
        for j in range(1,total+1):
            if arr[i] > j and i==0:
                lis[i][j] = 0
            elif arr[i] <= j and i==0:
                lis[i][j] = 1
            elif arr[i] > j:
                lis[i][j] = lis[i-1][j]
            else:
                lis[i][j] = lis[i-1][j] + lis[i][j-arr[i]]
                
    return lis[n-1][total]

total = int(input())
arr = list(map(int,input().split()))
print(ways_of_coins(arr, total, len(arr)))
