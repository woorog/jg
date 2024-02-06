import sys

N,tc=map(int, sys.stdin.readline().split())
numlist=[]
for _ in range(N):
    numlist.append(list(map(int, sys.stdin.readline().split())))


cumulative_sum = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        cumulative_sum[i][j] = numlist[i][j]
        if i > 0: cumulative_sum[i][j] += cumulative_sum[i-1][j]
        if j > 0: cumulative_sum[i][j] += cumulative_sum[i][j-1]
        if i > 0 and j > 0: cumulative_sum[i][j] -= cumulative_sum[i-1][j-1]

# 각 쿼리에 대한 구간 합 계산
for i in range(tc):
    query=[]
    query.append(map(int, sys.stdin.readline().split()))
    for  S_x, S_y, E_x, E_y in query:

        # 좌표는 0부터 시작하므로, 인덱스 조정
        S_x -= 1
        S_y -= 1
        E_x -= 1
        E_y -= 1

        # 누적합을 이용한 구간 합 계산
        range_sum = cumulative_sum[E_x][E_y]
        if S_x > 0: range_sum -= cumulative_sum[S_x-1][E_y]
        if S_y > 0: range_sum -= cumulative_sum[E_x][S_y-1]
        if S_x > 0 and S_y > 0: range_sum += cumulative_sum[S_x-1][S_y-1]

        print(range_sum)

