from collections import defaultdict

class Graph:
  
    def __init__(self,vertices):
        self.V= vertices
        self.graph = defaultdict(list)

    def addEdge(self,v,w):
        self.graph[v].append(w)
        self.graph[w].append(v) 

    def isCyclicUtil(self,v,visited,parent):
 
        visited[v]= True
        for i in self.graph[v]:
            if  visited[i]==False : 
                if(self.isCyclicUtil(i,visited,v)):
                    return True
            elif  parent!=i:
                return True
         
        return False
    def isCyclic(self):
        visited =[False]*(self.V)
        for i in range(self.V):
            if visited[i] ==False:
                if(self.isCyclicUtil(i,visited,-1))== True:
                    return True
         
        return False

vertex, m = map(int,input().split())
g = Graph(vertex)
for i in range(m):
    u, v = map(int,input().split())
    g.addEdge(u-1, v-1)

if m!=vertex-1 or vertex==1:
    print("NO")
else:
    if g.isCyclic():
        print("NO")
    else:
        print("YES")
    
