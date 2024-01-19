from collections import deque

def bfs(graph, start, K):
    distance = [-1] * (len(graph) + 1)  # 각 도시까지의 거리를 저장할 리스트, 초기값은 -1
    distance[start] = 0
    queue = deque([start])

    while queue:
        current = queue.popleft()

        for next in graph[current]:
            if distance[next] == -1:  # 아직 방문하지 않은 도시인 경우
                distance[next] = distance[current] + 1
                queue.append(next)

    return [city for city, dist in enumerate(distance) if dist == K]

# 입력 처리
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

# BFS 실행 및 결과 출력
result = bfs(graph, X, K)

if result:
    for city in sorted(result):
        print(city)
else:
    print(-1)
