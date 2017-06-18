n, m = map(int,input().split())
visited = [[False]*m for i in range(n)]
matrix = []
queue = []
ans_sheep, ans_wolf = 0, 0

for _ in range(n):
    arr = input()
    matrix.append(arr)

for i in range(n):
    for  j in range(m):
        sheep, wolf, flag = 0, 0, 0
        if visited[i][j]==False and matrix[i][j]!="#":
            queue.insert(-1, (i, j))
            while queue:
                x,y = queue[0][0],queue[0][1]
                queue.pop(0)
                if visited[x][y]==False:
                    visited[x][y] = True
                    
                    if matrix[x][y]=="v":
                        wolf+=1
                    elif matrix[x][y]=="k":
                        sheep+=1

                    if x==n-1 or x==0 or y==0 or y==m-1:
                        flag = 1

                    if x<n-1 and matrix[x+1][y]!="#":
                        queue.insert(-1, (x+1,y))
                        
                    #if x>0 and matrix[x-1][y]!="#":
                    #queue.insert(-1, (x-1,y))
                        
                    if y<m-1 and matrix[x][y+1]!="#":
                        queue.insert(-1, (x,y+1))

                    #if y>0and matrix[x][y-1]!="#":
                    #queue.insert(-1, (x,y-1))

            if flag == 0:
                if sheep>wolf:
                    ans_sheep+=sheep
                else:
                    ans_wolf+=wolf
            else:
                ans_sheep+=sheep
                ans_wolf+=wolf

print(ans_sheep, ans_wolf)
