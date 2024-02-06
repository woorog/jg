import sys
from collections import deque

class Graph:
    def __init__(self, num_vertices):
        self.graph = {i: [] for i in range(1, num_vertices + 1)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        #self.graph[v].append(u)


#다익스트라는 bfs 에서 무엇이 추가된 것일까

#하나의 최단 거리를 구할 때, 그 이전까지 구했던 최단 거리 정보를 그대로 사용한다.
def bfs_dijkstra(g, start, K):
    distances = {node: float('inf') for node in g.graph}
    distances[start] = 0

    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        for neighbor in g.graph[vertex]:  # 현재 노드(vertex)에 연결된 모든 이웃 노드(neighbor)에 대하여 반복
            new_distance = distances[vertex] + 1  # 이웃 노드까지의 새로운 거리 계산 (현재 노드까지의 거리 + 1)
            print(distances)
            print(neighbor)
            if new_distance < distances[neighbor]:  # 새로운 거리가 기존에 저장된 거리보다 작은지 확인
                distances[neighbor] = new_distance  # 새로운 거리가 더 작다면, 이웃 노드까지의 거리를 업데이트
                queue.append(neighbor)  # 업데이트된 거리를 가진 이웃 노드를 큐에 추가 (추후 탐색을 위해)




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
result = bfs_dijkstra(g, X, K)

