import sys
from collections import deque
class Graph:
    def __init__(self, num_vertices):
        self.graph = {i: [] for i in range(1, num_vertices + 1)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)





def bfs(graph, start):
    visited = set()
    queue = deque([start])
    count=0
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            #print(vertex, end=' ')

            # 인접 노드 중 방문하지 않은 노드를 큐에 추가
            for node in graph[vertex]:

                if node not in visited and vertexnum[node]=='0':

                    queue.append(node)
                elif node not in visited and vertexnum[node]=='1':
                    count +=1


    return count


def connected_components(graph):
    visited = set()
    count = 0
    #vertex 는 정점.

    for vertex in graph:
        # 이 과정에서 아직 방문하지 않은 정점을 찾을 때마다 연결 요소의 수를 하나씩 증가시킵니다.
        #print(vertexnum[vertex])
        if vertexnum[vertex]=='1':

            a=bfs(graph, vertex)
            count+=a

    return count

# 예제 그래프 생성
num = int(sys.stdin.readline())
vertexnum=[-1]
number=str(sys.stdin.readline())

for i in str(number):
    vertexnum.append(i)

g=Graph(num)

#print(vertexnum)
for _ in range(num-1):
    edge=list(map(int, sys.stdin.readline().split()))
    g.add_edge(edge[0],edge[1])


print(connected_components(g.graph))


