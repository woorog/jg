import sys

maze = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 높이 H, 행 M, 열 N을 입력받습니다.
input = sys.stdin.readline
M,N,H = map(int,input().rstrip().split())

box = [[list(map(int,input().rstrip().split())) for _ in range(N)] for _ in range(H)]


# 3차원 배열 출력하여 확인
# for h in range(H):
#     for m in range(M):
#         print(boxes[h][m])
#     print()  # 각 높이마다 줄바꿈으로 구분

print(boxes)