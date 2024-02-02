import copy
import heapq
import sys
from collections import deque


class Graph:
    def __init__(self, num):
        self.graph = {i: [] for i in range(1, num + 1)}


    def add_edge(self,u,v,cost):
        self.graph[u].append((v,cost))





def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        # 현재 정점과 해당 정점까지의 거리를 큐에서 추출

        if distances[current_vertex] < current_distance:
            continue
        # 현재 정점까지의 거리가 이미 알려진 최단 거리보다 크면 이 정점은 무시
        # (이미 더 짧은 경로를 통해 처리되었음

        # 현재 정점에서 인접한 모든 정점에 대해 반복
        for neighbor, weight in graph.graph[current_vertex]:
        # 현재 정점을 거쳐 이웃 정점으로 가는 거리 계산
            distance = current_distance + weight


        # 계산된 거리가 기존에 알려진 이웃 정점까지의 거리보다 짧으면 업데이트

        if distance < distances[neighbor]:
                distances[neighbor] = distance
                # 업데이트된 거리와 이웃 정점을 우선순위 큐에 추가
                heapq.heappush(queue, (distance, neighbor))

    return distances


N,tc,point=list(map(int,sys.stdin.readline().split()))
g=Graph(N)
edges=[]
for _ in range(tc):
    edges.append(list(map(int,sys.stdin.readline().split())))



graph = Graph(N)
for u, v, w in edges:
    graph.add_edge(u, v, w)

# 역방향 그래프 초기화 및 간선 추가
reverse_graph = Graph(N)
for u, v, w in edges:
    reverse_graph.add_edge(v, u, w)

# 각 정점에서 X로 가는 최단 경로
distances_to_X = dijkstra(graph, point)

# X에서 각 정점으로 돌아오는 최단 경로
distances_from_X = dijkstra(reverse_graph, point)

# 각 학생의 오고 가는데 걸리는 최대 시간 계산
max_time = 0
for node in graph.graph:
    time = distances_to_X[node] + distances_from_X[node]
    max_time = max(max_time, time)

print(max_time)

