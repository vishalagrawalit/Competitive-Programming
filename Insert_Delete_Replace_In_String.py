def distance(x,y,n,m):
    lis = [[0]*(m+1) for x in range(n+1)]
    
    for i in range(n+1):
        for j in range(m+1):
            if i==0:
                lis[i][j] = j
            elif j==0:
                lis[i][j] = i
            elif x[i-1]==y[j-1]:
                lis[i][j] = lis[i-1][j-1]
            else:
                lis[i][j]= 1+min(lis[i-1][j-1] , lis[i][j-1] , lis[i-1][j])
    return lis[n][m]
    
for _ in range(int(input())):
    s = input().split()
    n,m = int(s[0]),int(s[1])
    string = input().split()
    x,y = string[0],string[1]
    
    print(distance(x,y,n,m))
