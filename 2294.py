import sys
from collections import deque


def bfs(k, coins):
    queue = deque()
    queue.append((0, 0))  # (현재 금액, 사용한 동전 수)
    visited = set()  # 방문한 금액 추적

    while queue:
        current_sum, coin_count = queue.popleft()

        if current_sum == k:
            return coin_count

        for coin in coins:
            next_sum = current_sum + coin

            if next_sum <= k and next_sum not in visited:
                queue.append((next_sum, coin_count + 1))
                visited.add(next_sum)

    return -1  # 목표 금액을 만들 수 없는 경우

#내가 틀린 이유 visited 를 안만들어서.


N=list(map(int, sys.stdin.readline().split()))
coins=[int(sys.stdin.readline().strip()) for _ in range(N[0])]


print(bfs(N[1], coins))




def min_coins(coins, k):
    # 각 금액에 대한 최소 동전 개수를 저장할 배열 초기화
    dp = [float('inf')] * (k + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, k + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[k] if dp[k] != float('inf') else -1

# 입력
# n, k = map(int, input().split())
# coins = [int(input().strip()) for _ in range(n)]
#
# # 출력
# print(min_coins(coins, k))

#이 코드는 동적 프로그래밍을 이용하여 각 금액에 대해 필요한 최소 동전 개수를 계산합니다.
# 각 동전을 사용하여 만들 수 있는 금액의 최소 동전 개수를 dp 배열에 저장하고,
# 이를 재사용하여 최종 금액에 대한 최소 동전 개수를 계산합니다.