def bfs(matrix, e_x, e_y, m, n, visited, queue):
    while queue:
        x, y = queue[0][0],queue[0][1]
        queue.pop(0)

        if x==e_x and y==e_y:
            return visited[x][y]

        if x>0 and matrix[x-1][y]!="*" and visited[x-1][y]>visited[x][y]+1:
            visited[x-1][y]=visited[x][y]+1
            queue.append((x-1, y))

        if y>0 and matrix[x][y-1]!="*" and visited[x][y-1]>visited[x][y]+1:
            visited[x][y-1]=visited[x][y]+1
            queue.append((x, y-1))

        if x<m-1 and matrix[x+1][y]!="*" and visited[x+1][y]>visited[x][y]+1:
            visited[x+1][y]=visited[x][y]+1
            queue.append((x+1, y))

        if y<n-1 and matrix[x][y+1]!="*" and visited[x][y+1]>visited[x][y]+1:
            visited[x][y+1]=visited[x][y]+1
            queue.append((x, y+1))
    return -1

MAX = 10**5
for _ in range(int(input())):
    m, n = map(int,input().split())
    matrix = []
    for i in range(m):
        arr = input()
        matrix.append(arr)

    visited = [[MAX]*n for _ in range(m)]
    flag,count = 0,0
    queue = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j]=="$":
                s_x = i
                s_y = j
                visited[i][j]=0
                queue.append((i,j))
            if matrix[i][j]=="#":
                e_x = i
                e_y = j
    
    print(bfs(matrix, e_x, e_y, m, n, visited, queue))
