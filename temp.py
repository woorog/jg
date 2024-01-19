class graph:
    def __init__(self):
        self.graph={}  #[] 안쓰는 이유는 딕셔너리로 관리하기 위해 {} 선언

    def __str__(self):
        return str(self.graph)

    def insert_graph(self,n,m):
        if n in self.graph:
            self.graph[n].append(m)
        else:
            self.graph[n]=[m]
        if m in self.graph:
            self.graph[m].append(n)
        else:
            self.graph[m]=[n]


def dfs(graph,start,visited=None):
    if visited is None:
        visited=set()

    visited.add(start)
    print(start,end=' ')


    for next in graph[start]:
        if next not in visited:
            dfs(graph,next,visited)



def bfs(graph,start,visited=None):
    visited=set()



gp=graph()

gp.insert_graph(2,3)
gp.insert_graph(1,2)
gp.insert_graph(3,4)
gp.insert_graph(1,4)
gp.insert_graph(1,5)
gp.insert_graph(2,6)

print(gp.graph.get(2))
#print(gp:3)

