N, M = map(int,input().split())
while N!=0 and M!=0:
    matrix = []
    answer = []

    for i in range(N):
        arr = list(map(int,input().split()))
        matrix.append(arr)

    visited = [[False]*M for i in range(N)]
    queue = []

    for i in range(N):
        for j in range(M):
            if matrix[i][j]==1 and visited[i][j]==False:
                visited[i][j]=True
                queue.insert(0, (i,j))
                add=1

                while queue:
                    x, y = queue[0][0], queue[0][1]
                    queue.pop(0)
                    #print(queue.pop(0))

                    if x>0 and matrix[x-1][y]==1 and visited[x-1][y]==False:
                        visited[x-1][y]=True
                        queue.insert(0, (x-1, y))
                        add+=1
                    
                    if x<N-1 and matrix[x+1][y]==1 and visited[x+1][y]==False:
                        visited[x+1][y]=True
                        queue.insert(0, (x+1, y))
                        add+=1

                    if y>0 and matrix[x][y-1]==1 and visited[x][y-1]==False:
                        visited[x][y-1]=True
                        queue.insert(0, (x, y-1))
                        add+=1
                    
                    if y<M-1 and matrix[x][y+1]==1 and visited[x][y+1]==False:
                        visited[x][y+1]=True
                        queue.insert(0, (x, y+1))
                        add+=1

                answer.append(add)

    print(len(answer))
    answer.sort()
    ans = 0
    while ans<len(answer):
        print(answer[ans], answer.count(answer[ans]))
        ans+=answer.count(answer[ans])
    N, M = map(int,input().split())
    
                    
