from collections import deque
import sys

# 하나의 최단 거리를 구할 때, 그 이전까지 구했던 최단 거리 정보를 그대로 사용한다.
def bfs():
    queue = deque()
    queue.append((0, 0))
    visited = [[-1] * N for _ in range(N)]
    visited[0][0] = 0
    # bfs는 각 함수 호출마다 새로운 visited 집합과 queue를 생성합니다.
    # popleft(): deque의 메소드로, 큐의 맨 앞에서 요소를 제거하고 반환합니다


    while queue:
        x, y = queue.popleft()
        if x == N - 1 and y == N - 1:  # 마지막 방문했을때.
            return visited[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1: # 둘다 미로 범위 안에있고 방문 안했을때
                if maze[nx][ny] == 1:  # 흰방일때 탐색을 우선 하기 위해 앞에다가 추가
                    queue.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                    print(queue)
                else:
                    queue.append((nx, ny)) #검은방
                    visited[nx][ny] = visited[x][y] + 1

N,M = (map(int, sys.stdin.readline().split()))
ice = []
print(N,M)
for i in range(N):
    ice.append(list(map(int, sys.stdin.readline().split())))

bigver=max(map(min,ice))
print(bigver)
print(ice)

icedict={}


#진행할때마다 처음 모두 방문해야 하는
