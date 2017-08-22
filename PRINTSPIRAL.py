for x in range(int(input())):
    m, n = map(int,input().split())

    matrix = [[-1]*n]*m
    
    k, l = 0, 0
    last = 1
    while k<m and l<n:
        print(matrix)
        for i in range(l,n):
            if last < 10:
                last = "0"+str(last)
                matrix[k][i] = last
            else:
                matrix[k][i] = last
            last = int(last) + 1
        k+=1

        for i in range(k, m):
            if last < 10:
                last = "0"+str(last)
                matrix[i][n-1] = last
            else:
                matrix[i][n-1] = last
            last = int(last) + 1
        n-=1

        if k<m:
            for i in range(n-1, 0, -1):
                if last < 10:
                    last = "0"+str(last)
                    matrix[m-1][i] = last
                else:
                    matrix[m-i][i] = last
                last = int(last) + 1
            m-=1
        
        if l<n:
            for i in range(m-1, k-1, -1):
                if last < 10:
                    last = "0"+str(last)
                    matrix[i][1] = last
                else:
                    matrix[i][1] = last
                last = int(last) + 1
            l+=1

    print("Case ",x,":")
    for i in range(m):
        print(*matrix[i], sep=" ")
