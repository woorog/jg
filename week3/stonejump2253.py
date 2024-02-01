import sys

end,N = (map(int, sys.stdin.readline().split()))
small_stones=[int(sys.stdin.readline().strip()) for _ in range(N)]
def min_jumps(N, small_stones):
    # 최대 점프 거리 계산
    max_jump = int((2 * N) ** 0.5) + 1

    # DP 배열 초기화 (무한대로 설정)
    dp = [[float('inf')] * (max_jump + 1) for _ in range(N + 1)]
    dp[2][1] = 1  # 초기 조건 설정

    # 점프할 수 없는 돌들 설정
    cannot_jump = [False] * (N + 1)
    for stone in small_stones:
        cannot_jump[stone] = True

    # 각 돌에 대해 반복하며 DP 배열 갱신
    for i in range(2, N + 1):
        if cannot_jump[i]:
            continue
        for j in range(1, max_jump):
            if i - j > 0:
                dp[i][j] = min(dp[i][j], dp[i - j][j - 1] + 1, dp[i - j][j] + 1, dp[i - j][j + 1] + 1)

    # 마지막 돌에 도달하는 최소 점프 횟수를 찾기
    min_jumps = min(dp[N])
    return min_jumps if min_jumps != float('inf') else -1

# 예제 입력
# 예제 출력
print(min_jumps(end, small_stones))