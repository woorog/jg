import sys
from collections import deque

INF=int(1e9)


#다익스트라는 bfs 에서 무엇이 추가된 것일까

#하나의 최단 거리를 구할 때, 그 이전까지 구했던 최단 거리 정보를 그대로 사용한다.

# 예제 그래프 생성

num = int(sys.stdin.readline())
inputs = int(sys.stdin.readline())

# 2차원 리스트 (그래프 표현) 만들고, 무한대로 초기화
graph = [[INF] * (num + 1) for _ in range(num + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, num + 1):
    for b in range(1, num + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(inputs):
    # A -> B로 가는 비용을 C라고 설정
    a, b, c =map(int, sys.stdin.readline().split())
    # 기존에 설정된 비용과 새로운 비용 중 더 작은 것으로 갱신
    graph[a][b] = min(graph[a][b], c)


for k in range(1, num + 1):
    for a in range(1, num + 1):
        for b in range(1, num + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, num + 1):
    for b in range(1, num + 1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()

