import sys
from collections import deque


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(apt, a, b):
    n = len(apt)
    queue = deque()
    queue.append((a, b))
    apt[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if  0 <= nx < n and 0 <= ny < n and apt[nx][ny] == 1 :
                count += 1
                apt[nx][ny] = count #어차피 1보다 크니까 다음에 실행안됨
                queue.append((nx, ny))

    return count

n = int(sys.stdin.readline())
apt = []
for i in range(n):
    apt.append(list(map(int, sys.stdin.readline().strip())))

ans = []

for i in range(n):
    for k in range(n):
        if apt[i][k] == 1:
            ans.append(bfs(apt, i, k))

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])