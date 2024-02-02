import sys
from collections import deque

N,M=map(int, sys.stdin.readline().split())
maze = []
for i in range(N):
    maze.append(list(map(int, input().strip())))
# BFS 함수 정의
def bfs():
    # 방문 체크 및 거리 계산을 위한 3차원 배열 초기화
    visited = [[[0]*2 for _ in range(M)] for __ in range(N)]
    queue = deque()
    # (x, y, 벽을 부순 상태)
    queue.append((0, 0, 0))
    visited[0][0][0] = 1  # 시작 위치 방문 체크

    # 상, 하, 좌, 우 이동 방향
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while queue:
        x, y, wall = queue.popleft()

        # 도착 지점에 도달한 경우
        if x == N-1 and y == M-1:
            return visited[x][y][wall]

        # 현재 위치에서 4방향으로 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 이동 가능한 위치인 경우
            if 0 <= nx < N and 0 <= ny < M:
                # 빈 칸으로 이동하는 경우
                if maze[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    queue.append((nx, ny, wall))
                # 벽을 만나고 아직 벽을 부수지 않은 경우
                elif maze[nx][ny] == 1 and wall == 0:
                    visited[nx][ny][1] = visited[x][y][wall] + 1
                    queue.append((nx, ny, 1))

    # 도착 지점에 도달할 수 없는 경우
    return -1

# BFS 실행 및 결과 출력
bfs_result = bfs()
print(bfs_result)

