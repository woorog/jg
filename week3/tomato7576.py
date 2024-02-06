import sys
from collections import deque

M, N= (map(int, sys.stdin.readline().split()))
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(box):
    queue = deque()
    visited =[[-1] * M for _ in range(N)]

    for l in range(N):
        for k in range(M):
            if box[l][k] == 1:
                visited[l][k] = 0
                queue.append((l, k))
            elif box[l][k] == -1:
                visited[l][k] = 0


    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == -1:
                queue.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1

    return visited



endbox = bfs(box)
max_day = 0
iszero = 0




for j in range(N):
    for k in range(M):
        if endbox[j][k] == -1 and box[j][k] == 0:
            iszero = 1
        else:
            max_day = max(max_day, endbox[j][k])


if iszero == 1:
    print(-1)
else:
    print(max_day)
