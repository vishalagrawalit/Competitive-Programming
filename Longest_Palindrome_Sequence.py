def palindrome(string , n):
    lis = [[0]*n for x in range(n)]

    for i in range(n):
        lis[i][i]=1

    for x in range(2,n+1):
        for y in range(n-x+1):
            j = x+y - 1
            if string[y]==string[j] and x==2:
                lis[y][j] = 2
            elif string[y]==string[j]:
                lis[y][j] = 2 + lis[y+1][j-1]
            else:
                lis[y][j] = max(lis[y+1][j] , lis[y][j-1])
    return lis[0][n-1]

string = input()
print(palindrome(string, len(string)))
