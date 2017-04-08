def seq(x,y,m,n):
    
    lis = [[None]*(n+1) for i in range(m+1)]
    for j in range(m+1):
        for k in range(n+1):
            if j==0 or k==0:
                lis[j][k]=0
            elif x[j-1]==y[k-1]:
                lis[j][k]=lis[j-1][k-1]+1
            else:
                lis[j][k]=max(lis[j][k-1] , lis[j-1][k])
            
    return lis[m][n]
    
    
for _ in range(int(input())):
    s = input().split()
    x,y = input(),input()
    print(seq(x,y,int(s[0]),int(s[1])))
