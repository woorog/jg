import sys
input = sys.stdin.readline
from collections import deque
import heapq

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

virusList = [[] for _ in range(M+1)]

second, X, Y = map(int, input().split())

limitTime = second

def GetVirus():
    global limitTime
    time = 0

    que = deque()

    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                virusList[graph[i][j]].append((graph[i][j], i, j))
                # que.append((graph[i][j], i, j))
                # heapq.heappush(heap, (graph[i][j], i, j))

    for i in range(1, len(virusList)):
        for pos in virusList[i]:
            que.append(pos)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while que:
        for _ in range(len(que)):
            # print(que)
            # val, x, y = heapq.heappop(heap)
            val, x, y = que.popleft()

            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]

                if 0 <= nx < N and 0 <= ny < N:
                    if graph[nx][ny] <= 0:
                        graph[nx][ny] = val
                        que.append((graph[nx][ny], nx, ny))
                        # heap.append((graph[nx][ny], nx, ny))
        time += 1
        if time >= limitTime:
            return

GetVirus()
print(graph[X-1][Y-1])