def puzzle(n,k):
    lis = [[0]*(k+1) for x in range(n+1)]

    for i in range(n+1):
        for j in range(k+1):
            if j==1 or j==0:
                lis[i][j] = j
            elif i==1:
                lis[i][j] = j
                

for _ in range(int(input())):
    s = input().split()
    n,k=int(s[0]),int(s[1])
    print(puzzle(n,k))
