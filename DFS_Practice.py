from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, x, y):
        self.graph[x].append(y)
        
    def DFS(self):
        visited = [False]*len(self.graph)
        
        for i in range(len(self.graph)):
            if visited[i]==False:
                self.DFSUtil(i, visited)
                
    def DFSUtil(self, v, visited):
        
        visited[v] = True
        print(v)
        
        for j in self.graph[v]:
            if visited[j]==False:
                self.DFSUtil(j, visited)
                
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
g.DFS()
