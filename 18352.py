import sys
from collections import deque

class Graph:
    def __init__(self, num_vertices):
        self.graph = {i: [] for i in range(1, num_vertices + 1)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        #self.graph[v].append(u)



def dijkstra(graph, start, K):
    distances = {node: float('inf') for node in graph.graph}
    distances[start] = 0
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        for neighbor in graph.graph[vertex]:
            new_distance = distances[vertex] + 1
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                queue.append(neighbor)


    result = []
    for node, distance in distances.items():  # 딕셔너리 순회는 이렇게 하면 편함
        if distance == K:
            result.append(node)


    return result


# 예제 그래프 생성
N, M, K, X =map(int, sys.stdin.readline().split())  # 예제 입력
g = Graph(N)

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    g.add_edge(A, B)

# 다익스트라 알고리즘 실행
result = dijkstra(g, X, K)

if result:
    for city in result:
        print(city)
else:
    print(-1)