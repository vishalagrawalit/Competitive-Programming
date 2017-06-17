from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, x, y):
        self.graph[x].append(y)
    
    def Cycle(self):
        visited = [False]*(len(self.graph))
        stack = [False]*(len(self.graph))
        
        for i in range(len(self.graph)):
            if visited[i]==False:
                if self.isCyclic(i, visited, stack)==True:
                    return True
        return False
        
    def isCyclic(self, v, visited, stack):
        visited[v], stack[v]=True, True
        for neighbour in self.graph[v]:
            if visited[neighbour]==False:
                if self.isCyclic(neighbour, visited, stack)==True:
                    return True
            elif stack[neighbour]==True:
                return True
                
        stack[v]=False
        return False
        
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.Cycle() == True:
    print ("Graph has a cycle")
else:
    print ("Graph has no cycle")
                
