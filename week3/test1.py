import sys

num=int(sys.stdin.readline())
listnum = [int(sys.stdin.readline().strip()) for _ in range(num)]
def maxs(stairs):
    n = len(stairs)
    if n == 1:
        return stairs[0]

    # DP 배열 초기화
    dp = [0] * n
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]

    for i in range(2, n):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i]) #  현재는 한칸 오르거나 두칸 오른걸 기준

    return dp[-1]

print(maxs(listnum))