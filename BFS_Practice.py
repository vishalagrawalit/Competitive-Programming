from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, x, y):
        self.graph[x].append(y)
    
    def BFS(self):
        
        visited = [False]*(len(self.graph))
        queue = []
        
        for i in range(len(self.graph)):
            if visited[i]==False:
                queue.append(i)
                visited[i]=True
                
                while queue:
                    s = queue.pop(0)
                    print(s)
                    
                    for j in self.graph[s]:
                        if visited[j]==False:
                            queue.append(j)
                            visited[j] = True
                        
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.BFS()
