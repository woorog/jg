import sys

num=int(sys.stdin.readline())

numlist=list(map(int,sys.stdin.readline().split()))

# print(numlist)
# dp = [0] * (num+1)
# for k in range(num):
#
#     coin=k+1
#     cost=numlist[k]
#     dp[1]=numlist[k]
#     for i in range(2, num+1):
#         if i>coin:
#             dp[i] = max(dp[i], dp[i - coin] + cost)
#     print(dp)


def max_price(N, card):
    # 다이내믹 프로그래밍을 위한 배열 초기화
    dp = [0] * (N + 1)

    # 모든 카드팩에 대해 최대 금액 계산
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            if i - j >= 0:
                dp[i] = max(dp[i], dp[i - j] + card[j - 1])

    return dp[N]


print(max_price(num,numlist))