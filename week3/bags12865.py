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
        print(dp)

    print()
    print(dp)

print(max(dp))


#0-1 배낭 문제 (0-1 Knapsack Problem): 이 문제에서는 각 물건을 하나만 가지고 있으며, 각 물건을 배낭에 넣거나 넣지 않는 선택을 합니다.
# 이 경우, 동적 프로그래밍 배열(dp)을 업데이트할 때 역순 루프를 사용하는 것이 중요합니다. 역순으로 처리하지 않으면, 같은 물건을 여러 번 고려할 수 있기 때문입니다.
#----> 그니까 0-1 배낭 문제를 풀때는 중복이 가능하면 정방향으로  중복이 불가능하면 역방향으로

## 만약 배낭 문제가 "여러 번 선택할 수 있는" 경우, 즉 한 물건을 여러 번 배낭에 넣을 수 있는
# '무제한 배낭 문제'(Unbounded Knapsack Problem)라면,
# 동적 프로그래밍 배열을 역순이 아닌 정순(1부터 증가하는 순서)으로 업데이트합니다

#배낭의 갯수 제한이 있는 배낭 문제: 이 유형의 문제에서는 배낭이 여러 개 있으며, 각 배낭마다 무게 제한이 다를 수 있습니다.
# 이 경우 문제의 풀이는 문제의 구체적인 조건에 따라 달라집니다. 일반적으로 이 문제는 다차원 동적 프로그래밍 문제로 해결될 수 있으며,
# 항상 역순으로 풀어야 하는 것은 아닙니다.


#따라서, "갯수가 정해져 있는 배낭 문제"라는 표현이 0-1 배낭 문제를 의미한다면, 네, 역순으로 처리하는 것이 중요합니다.
# 하지만 다른 유형의 배낭 문제를 말한다면, 해결 방법은 문제의 세부 사항에 따라 달라질 수 있습니다.
