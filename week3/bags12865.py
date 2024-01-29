import sys

N, M = (map(int, sys.stdin.readline().split()))

bags = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [0] * (M + 1)
# for k in range(N):
#
#
#     dp[0] = bags[k][1]
#     coin = bags[k][0]
#
#     for i in range(1, M + 1):
#         if i >= coin:
#             if i==coin:
#                 dp[i]>dp[0]
#                 dp[i]=dp[0]
#             elif dp[i] < dp[i-coin]+dp[coin]:
#                 dp[i] = dp[i-coin]+dp[coin]
#
# print(max(dp))
# bags.sort(reverse=True)
# for k in range(N):
#
#
#     cost = bags[k][1]
#     coin = bags[k][0]
#
#     for i in range(1, M + 1):
#         if i== coin:
#             dp[i]<cost
#             dp[i]=cost
#
#         if i > coin:
#             if dp[i] < dp[i-coin]+dp[coin]:
#                 dp[i] = dp[i-coin]+dp[coin]
#     print(dp)
for coin, cost in bags:
    for i in range(M, coin - 1, -1):
        dp[i] = max(dp[i], dp[i - coin] + cost)


print(max(dp))
