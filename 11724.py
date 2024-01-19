import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
class Graph:
    def __init__(self, num_vertices):
        self.graph = {i: [] for i in range(1, num_vertices + 1)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)





def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            #print(vertex, end=' ')

            # 인접 노드 중 방문하지 않은 노드를 큐에 추가
            for node in graph[vertex]:
                if node not in visited:
                    queue.append(node)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set() #중복을 허용하지 않는 set 을 사용해 넣어줌 visited 집합을 재귀 호출에서 공유하기 위함

    visited.add(start)
    #print(start, end=' ')

    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)

def connected_components(graph):
    visited = set()
    count = 0
    #vertex 는 정점.

    for vertex in graph:
        #print(vertex)
        # 이 과정에서 아직 방문하지 않은 정점을 찾을 때마다 연결 요소의 수를 하나씩 증가시킵니다.
        if vertex not in visited:
            dfs(graph, vertex, visited)
            count += 1

    return count

# 예제 그래프 생성
listnum= list(map(int, sys.stdin.readline().split()))
g = Graph(listnum[0])

for _ in range(listnum[1]):
    edge=list(map(int, sys.stdin.readline().split()))
    g.add_edge(edge[0],edge[1])

print(g.graph)


