import sys
from collections import deque


def bfs_modified(box):
    queue = deque()
    visited = [[[-1] * M for _ in range(N)] for _ in range(H)]
    for i in range(H):
        for l in range(N):
            for k in range(M):
                if box[i][l][k] == 1:
                    visited[i][l][k] = 0
                    queue.append((i, l, k))
                elif box[i][l][k] == -1:
                    visited[i][l][k] = 0
    while queue:
        z, y, x = queue.popleft()

        for direction in range(6):
            nx = x + dx[direction]
            ny = y + dy[direction]
            nz = z + dz[direction]

            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and visited[nz][ny][nx] == -1:
                queue.append((nz, ny, nx))
                visited[nz][ny][nx] = visited[z][y][x] + 1

    return visited
def all0(box):
    for layer in box:
        for row in layer:
            if any(cell == 0 for cell in row):
                return False
    return True
#이부분이 틀렸었음


def noway_modified(box):
    for i in range(H):
        for l in range(N):
            for k in range(M):
                if box[i][l][k] == 0:
                    isolated = True
                    for direction in range(6):
                        ni = i + dz[direction]
                        nl = l + dy[direction]
                        nk = k + dx[direction]
                        if 0 <= ni < H and 0 <= nl < N and 0 <= nk < M and box[ni][nl][nk] != -1:
                            isolated = False
                            break
                    if isolated:
                        return True
    return False

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# 높이 H, 행 M, 열 N을 입력받습니다.
#M, N, H = map(int, input().split())
M, N, H = (map(int, sys.stdin.readline().split()))
box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]




if noway_modified(box):
    print(-1)
elif all0(box):
    print(0)
else:
    visited = bfs_modified(box)
    max_day = 0

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if visited[i][j][k] == -1 and box[i][j][k] == 0:
                    print(-1)
                    sys.exit()
                    #이부분이 없어서 틀렸음...
                max_day = max(max_day, visited[i][j][k])

    print(max_day)


#visited[i][j][k] == -1:
#
# 이 조건은 BFS 탐색 중 해당 위치 (i, j, k)가 아직 방문되지 않았음을 나타냅니다.
# BFS 알고리즘에서는 탐색 가능한 모든 위치를 방문하면서, 각 위치에 도달하는 데 걸리는 시간(일수)을 visited 배열에 기록합니다.
# 만약 어떤 위치가 방문되지 않았다면 (visited[i][j][k] 값이 -1로 남아 있다면), 그 위치에 있는 토마토는 주변에 익은 토마토가 없어서 영향을 받지 못했음을 의미합니다.
# box[i][j][k] == 0:
#
# 이 조건은 해당 위치 (i, j, k)에 토마토가 있지만 아직 익지 않았음을 나타냅니다 (0은 익지 않은 토마토를 나타냄).
# 따라서, box[i][j][k] 값이 0인 경우는 해당 위치에 아직 익지 않은 토마토가 있음을 의미합니다.
# 이 두 조건이 동시에 충족될 때 (visited[i][j][k] == -1 및 box[i][j][k] == 0),
# 이는 BFS 탐색을 통해 모든 익은 토마토로부터 접근 가능한 위치를 방문했음에도 불구하고, 여전히 익지 않은 토마토가 존재한다는 것을 의미합니다.
# 즉, 창고 안에는 절대로 익지 못하는 토마토가 존재한다는 것입니다. 이 경우 프로그램은 -1을 출력하고 종료되어야 합니다.
# sys.exit() 함수는 프로그램을 즉시 종료시키는 역할을 합니다.

