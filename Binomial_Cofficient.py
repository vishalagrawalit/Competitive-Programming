def binomial(n,k):
    lis = [[0]*(k+1) for x in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j==0 or j==i:
                lis[i][j]=1
            else:
                lis[i][j] = lis[i-1][j-1] + lis[i-1][j]
    return lis[n][k]

n,k=int(input()),int(input())
print(binomial(n,k))
    
