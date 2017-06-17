from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, x, y):
        self.graph[x].append(y)
        self.graph[y].append(x)
    
    def Cycle(self):
        visited = [False]*len(self.graph)
        
        for i in range(len(self.graph)):
            if visited[i]==False:
                if self.IsCyclic(i, visited, -1)==True:
                    return True
                    
        return False
        
    def IsCyclic(self, v, visited, parent):
        visited[v]=True
        
        for neighbor in self.graph[v]:
            if visited[neighbor] == True:
                if parent!=neighbor:
                    return True
            else:
                if self.IsCyclic(neighbor, visited, v)==True:
                    return True
        
        return False
        
g = Graph()
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
 
if g.Cycle()==True:
    print ("Graph contains cycle")
else :
    print ("Graph does not contain cycle ")
g1 = Graph()
g1.addEdge(0,1)
g1.addEdge(1,2)
 
 
if g1.Cycle()==True:
    print ("Graph contains cycle")
else :
    print ("Graph does not contain cycle ")
