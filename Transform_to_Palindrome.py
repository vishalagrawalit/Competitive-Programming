from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self, s, loc):
        visited = [False]*(len(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True
        count = 0
 
        while queue:
            s = queue.pop(0)
            if s==loc:
                return True
            else:
                count+=1
                if count==vertex-1:
                    return False
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph()
n, k, m = map(int,input().split())
global vertex
vertex = n
for _ in range(k):
    x, y = map(int,input().split())
    g.addEdge(x, y)
    g.addEdge(y, x)

arr = list(map(int,input().split()))
count = 0
left, right = 0, m-1
while left<right:
    if arr[left] == arr[right]:
        count+=2
        left+=1
        right-=1
    else:
        if g.BFS(arr[right], arr[left]):
            arr[right] = arr[left]
            count+=2
            left+=1
            right-=1
        elif g.BFS(arr[left], arr[right]) :
            arr[left] = arr[right]
            count+=2
            left+=1
            right-=1
        else:
            right-=1

if m%2==0:
    print(count+1)
else:
    print(count)


            
