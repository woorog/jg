import sys

num,N = (map(int, sys.stdin.readline().split()))



coins=[int(sys.stdin.readline().strip()) for _ in range(num)]


dp = [0] * (N+1)

dp[0] = 1
for coin in coins:
    for i in range(1, N+1):
        if i >= coin:
            dp[i] += dp[i-coin]

print(dp[N])
