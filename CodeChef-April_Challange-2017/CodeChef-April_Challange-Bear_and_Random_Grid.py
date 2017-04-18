for _ in range(int(input())):
    s = input().split()
    l,n = int(s[0]),int(s[1])
    string = input()
    matrix = []
    lis=[[0]*n for a in range(n)]
    for m in range(n):
        q = input()
        for o in range(n):
            if q[o]==".":
                matrix.append((m,o))
                lis[m][o]=1
    
    ans = 0

    for x in range(len(matrix)):
        count,i,j=0,matrix[x][0],matrix[x][1]           
        for k in range(l):
            if (i==0 and string[k]=="U") or (i==n-1 and string[k]=="D"):
                break
            elif (j==0 and string[k]=="L") or (j==n-1 and string[k]=="R"):
                break
            elif string[k]=="D" and lis[i+1][j]==1:
                count+=1
                i+=1
            elif string[k]=="U" and lis[i-1][j]==1:
                count+=1
                i-=1
            elif string[k]=="L" and lis[i][j-1]==1:
                count+=1
                j-=1
            elif string[k]=="R" and lis[i][j+1]==1:
                count+=1
                j+=1
            else:
                break
        ans ^= count
    print(ans)
        
    
