import sys

num=int(sys.stdin.readline())
listnum=[]
for _ in range(num):
    listnum.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * num for _ in range(num)]

dp[0][0] = 1
for i in range(num):
    for j in range(num):
        if dp[i][j] > 0 and listnum[i][j] > 0:
            jump = listnum[i][j]
            if i + jump < num:
                dp[i + jump][j] += dp[i][j]
            if j + jump < num:
                dp[i][j + jump] += dp[i][j]
        print(dp)
print(dp[num-1][num-1])

#.py