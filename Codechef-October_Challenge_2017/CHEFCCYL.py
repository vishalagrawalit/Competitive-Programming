INF  = 99999
def floydWarshall(graph, V):
    dist = graph
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j] ,dist[i][k]+ dist[k][j])


for _ in range(int(input())):
    n, q = map(int, input().split())
    matrix = [[INF]*(10**6)]*(10**6)
    index = [0]*n
    x = 0
    for i in range(n):
        arr = list(map(int, input().split()))
        index[i] = arr[0]
        y = 0
        for j in range(1+x, x+arr[0]+1):
            matrix[i][j] = arr[y]
            y += 1
        x += arr[0]

    for i in range(1, n):
        index[i] += index[i-1]
        
    floydWarshall(matrix, index[n-1])
    for i in range(q):
        v1, c1, v2, c2 = map(int, input().split())
        if c1==1:
            source = v1
            destination = index[c2-2] + v2
        else:
            if c2==1:
                destination = v2
            else:
                destination = index[c2-2] + v2
        print(dist[source-1][destination-1])
        
        
