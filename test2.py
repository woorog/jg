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
            nx,ny=dx[k],dy[k]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==-1:
                if maze[nx][ny] == 1:
                    queue.appendleft((nx,ny))
                    visited[nx][ny]=visited[x][y]
                else:
                    queue.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1
        #그럼 마지막 방문했을때 가장 최솟값이 나오는 파이썬식 최솟값 구하기.

#appendleft는 deque의 왼쪽 끝에 원소를 추가
#여기서 appendleft는 미로에서 현재 위치 (nx, ny)가 1인 경우, 즉 이동 가능한 경로인 경우에 사용
#반면, append는 deque의 오른쪽 끝에 원소를 추가
#여기서 append는 현재 위치가 이동 불가능한 경로 (즉, 0인 경우)일 때 사용


# 예제 그래프 생성
N = int(sys.stdin.readline())
maze = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(N):
    maze.append(list(map(int, input().strip())))


print(bfs())

