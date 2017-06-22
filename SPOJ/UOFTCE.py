def bfs(matrix, counter, visited, queue):
    distance_from_car, maxi = 0, -1
    
    while queue:
        x, y = queue[0][0],queue[0][1]
        queue.pop(0)

        if matrix[x][y]=="S":
            if maxi < visited[x][y]:
                maxi = visited[x][y]
            distance_from_car+=visited[x][y]
            counter-=1

        if counter==0:
            return 2*distance_from_car - maxi

        if x>0 and matrix[x-1][y]!="#" and visited[x-1][y]>visited[x][y]+1:
            visited[x-1][y]=visited[x][y]+1
            queue.append((x-1, y))

        if y>0 and matrix[x][y-1]!="#" and visited[x][y-1]>visited[x][y]+1:
            visited[x][y-1]=visited[x][y]+1
            queue.append((x, y-1))

        if x<m-1 and matrix[x+1][y]!="#" and visited[x+1][y]>visited[x][y]+1:
            visited[x+1][y]=visited[x][y]+1
            queue.append((x+1, y))

        if y<n-1 and matrix[x][y+1]!="#" and visited[x][y+1]>visited[x][y]+1:
            visited[x][y+1]=visited[x][y]+1
            queue.append((x, y+1))

MAX = 10**9
for _ in range(int(input())):
    m, n = map(int,input().split())
    matrix = []
    for i in range(m):
        arr = input()
        matrix.append(arr)

    visited = [[MAX]*n for _ in range(m)]
    queue = []
    stores = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j]=="C":
                s_x = i
                s_y = j
                visited[i][j]=0
                queue.append((i,j))
            if matrix[i][j]=="S":
                stores+=1
    
    print(stores*60 + bfs(matrix, stores, visited, queue))
