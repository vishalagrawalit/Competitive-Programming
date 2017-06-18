f, s, g, u, d = map(int,input().split())
visited = [0]*1000010

queue = []
queue = [(s,0)]

while queue:
    floor = queue[0][0]
    steps = queue[0][1]

    queue.pop(0)

    if visited[floor]==1:
        continue

    visited[floor]=1

    if floor == g:
        print(steps)
        break
    
    if floor + u <= f:
        queue.append((floor+u, steps+1))

    if floor - d > 0:
        queue.append((floor-d, steps+1))
else:
    print("use the stairs")
    
