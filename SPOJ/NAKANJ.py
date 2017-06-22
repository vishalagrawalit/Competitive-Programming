def bfs(e_x, e_y, visited, queue):

    #These two lists define the moves!
    a, b = [2, 2, -2, -2, 1, -1, 1, -1], [1, -1, 1, -1, 2, 2, -2, -2]
    
    while queue:
        x, y = queue[0][0],queue[0][1]
        queue.pop(0)

        if x==e_x and y==e_y:
            return visited[x][y]

        for limit in range(8):
            t_x = x + a[limit]
            t_y = y + b[limit]

            if t_x>=0 and t_x<8 and t_y>=0 and t_y<8:
                if visited[t_x][t_y]>visited[x][y]+1:
                    visited[t_x][t_y]=visited[x][y]+1
                    queue.append((t_x, t_y))

MAX = 5000
for _ in range(int(input())):
    s = input().split()
    
    s_y = ord(s[0][0])-97
    s_x = int(s[0][1])-1
    e_y = ord(s[1][0])-97
    e_x = int(s[1][1])-1

    #print(s_x, s_y, e_x, e_y)

    #Declaring Queue & visited array which stores the minimum distance
    visited = [[MAX]*8 for _ in range(8)]
    queue = []

    #initialisation for start
    visited[s_x][s_y] = 0
    queue.append((s_x, s_y))
    
    print(bfs(e_x, e_y, visited, queue))
