for _ in range(int(input())):
    m, n = map(int,input().split())
    matrix = []
    for _ in range(m):
        arr = input()
        matrix.append(arr)

    points, dot_check = [], 0

    for i in range(n):
        if matrix[0][i]==".":
            dot_check += 1
            points.append((0,i))
            
        if m>1 and matrix[m-1][i]==".":
            dot_check += 1
            points.append((m-1,i))

    for i in range(1,m-1):
        if matrix[i][0]==".":
            dot_check += 1
            points.append((i,0))
            
        if n>1 and matrix[i][n-1]==".":
            dot_check += 1
            points.append((i,n-1))

    #print(dot_check)
    #print(points)
    if dot_check != 2:
        print("invalid")
    else:
        visited = [[False]*n for i in range(m)]
        queue, flag = [], -1

        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="." and visited[i][j]==False:
                    queue.insert(0, (i, j))

                    while queue:
                        x, y = queue[0][0],queue[0][1]
                        visited[x][y]=True
                        queue.pop(0)

                        if x<m-1 and matrix[x+1][y]=="." and visited[x+1][y]==False:
                            queue.insert(0, (x+1, y))

                        if x>0 and matrix[x-1][y]=="." and visited[x-1][y]==False:
                            queue.insert(0, (x-1, y))

                        if y<n-1 and matrix[x][y+1]=="." and visited[x][y+1]==False:
                            queue.insert(0, (x, y+1))

                        if y>0 and matrix[x][y-1]=="." and visited[x][y-1]==False:
                            queue.insert(0, (x, y-1))
                            

                start, end = points[0],points[1]
                if visited[start[0]][start[1]] == True and visited[end[0]][end[1]] == True:
                    flag = 1
                    break
                elif visited[start[0]][start[1]] == True and visited[end[0]][end[1]] == False:
                    flag=0
                    break
                elif visited[start[0]][start[1]] == False and visited[end[0]][end[1]] == True:
                    flag=0
                    break
            if flag==1:
                print("valid")
                break
            elif flag==0:
                print("invalid")
                break
for _ in range(int(input())):
    m, n = map(int,input().split())
    matrix = []
    for _ in range(m):
        arr = input()
        matrix.append(arr)

    points, dot_check = [], 0

    for i in range(n):
        if matrix[0][i]==".":
            dot_check += 1
            points.append((0,i))
            
        if m>1 and matrix[m-1][i]==".":
            dot_check += 1
            points.append((m-1,i))

    for i in range(1,m-1):
        if matrix[i][0]==".":
            dot_check += 1
            points.append((i,0))
            
        if n>1 and matrix[i][n-1]==".":
            dot_check += 1
            points.append((i,n-1))

    #print(dot_check)
    #print(points)
    if dot_check != 2:
        print("invalid")
    else:
        visited = [[False]*n for i in range(m)]
        queue, flag = [], -1

        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="." and visited[i][j]==False:
                    queue.insert(0, (i, j))

                    while queue:
                        x, y = queue[0][0],queue[0][1]
                        visited[x][y]=True
                        queue.pop(0)

                        if x<m-1 and matrix[x+1][y]=="." and visited[x+1][y]==False:
                            queue.insert(0, (x+1, y))

                        if x>0 and matrix[x-1][y]=="." and visited[x-1][y]==False:
                            queue.insert(0, (x-1, y))

                        if y<n-1 and matrix[x][y+1]=="." and visited[x][y+1]==False:
                            queue.insert(0, (x, y+1))

                        if y>0 and matrix[x][y-1]=="." and visited[x][y-1]==False:
                            queue.insert(0, (x, y-1))
                            

                start, end = points[0],points[1]
                if visited[start[0]][start[1]] == True and visited[end[0]][end[1]] == True:
                    flag = 1
                    break
                elif visited[start[0]][start[1]] == True and visited[end[0]][end[1]] == False:
                    flag=0
                    break
                elif visited[start[0]][start[1]] == False and visited[end[0]][end[1]] == True:
                    flag=0
                    break
            if flag==1:
                print("valid")
                break
            elif flag==0:
                print("invalid")
                break
