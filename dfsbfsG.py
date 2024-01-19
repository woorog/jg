import sys
from collections import deque

class Graph:
    def __init__(self, num_vertices):
        self.graph = {i: [] for i in range(1, num_vertices + 1)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

        self.graph[u].sort()
        self.graph[v].sort()

# 예제 그래프 생성

listnum= list(map(int, sys.stdin.readline().split()))
g = Graph(listnum[0])
for _ in range(listnum[1]):
    edge=list(map(int, sys.stdin.readline().split()))
    g.add_edge(edge[0],edge[1])



def bfs(graph, start):
    if start not in graph:
        print(start)
        return
    visited = set()
    queue = deque([start])

    #popleft(): deque의 메소드로, 큐의 맨 앞에서 요소를 제거하고 반환합니다
    #vertex: 큐에서 꺼낸 현재 탐색할 노드를 저장하는 변수
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')

            # 인접 노드 중 방문하지 않은 노드를 큐에 추가
            for node in graph[vertex]:
                if node not in visited:
                    queue.append(node)

def dfs(graph, start, visited=None):
    if start not in graph:
        print(start)
        return
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')

    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)


# DFS 실행

dfs(g.graph, listnum[2])
print()
# BFS 실행

bfs(g.graph, listnum[2])
