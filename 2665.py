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
                else:
                    queue.append((nx, ny)) #검은방
                    visited[nx][ny] = visited[x][y] + 1

        #그럼 마지막 방문했을때 가장 최솟값이 나오는 파이썬식 최솟값 구하기.

#appendleft는 deque의 왼쪽 끝에 원소를 추가
#여기서 appendleft는 미로에서 현재 위치 (nx, ny)가 1인 경우, 즉 이동 가능한 경로인 경우에 사용
#반면, append는 deque의 오른쪽 끝에 원소를 추가
#여기서 append는 현재 위치가 이동 불가능한 경로 (즉, 0인 경우)일 때 사용

#이차원 배열 사용 이유
#간결성: 이차원 배열을 사용하면 복잡한 클래스 정의 없이 간단하게 그래프를 표현할 수 있습니다.
# 특히 파이썬에서는 리스트 내포(List Comprehension)를 사용하여 쉽고 빠르게 배열을 초기화할 수 있습니다.

#직관성: 격자 형태의 문제(예: 미로 탐색)에서 이차원 배열은 매우 직관적입니다.
# 배열의 각 요소가 격자의 각 칸에 대응하며, 인접한 칸은 배열에서도 인접한 요소로 표현됩니다.

#메모리 효율성: 대부분의 경우, 이차원 배열은 필요한 만큼의 공간만을 사용하며, 클래스 기반의 구조보다 메모리 효율이 좋을 수 있습니다.

#속도: 배열 기반의 접근은 파이썬에서 일반적으로 빠른 성능을 제공합니다.

#이차원 배열 사용 방법
#인접 행렬: 그래프의 노드 간 연결 여부를 행렬로 표현합니다. 예를 들어, graph[i][j]가 True 또는 1이면 노드 i와 j가 연결되어 있음을 나타냅니다.
# 이 방법은 주로 노드 수가 적은 밀집 그래프(Dense Graph)에 적합합니다.

#인접 리스트: 각 노드에 연결된 노드의 목록을 배열로 저장합니다. 예를 들어, graph[i]는 노드 i에 인접한 노드들의 목록을 나타냅니다.
# 이 방법은 희소 그래프(Sparse Graph)에서 메모리를 절약하는 데 유리합니다.

#격자 기반 그래프: 2차원 격자 형태의 문제에서는 각 격자 칸을 배열의 요소로 나타내며, 인접한 칸은 배열에서 상하좌우 인접한 요소로 표현됩니다.
# 예제 그래프 생성
N = int(sys.stdin.readline())
maze = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(N):
    maze.append(list(map(int, input().strip())))


print(bfs())


