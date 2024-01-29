import sys
N = int(sys.stdin.readline())
apts = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]
dp[0][0]=apts[0][0]
dp[0][1]=apts[0][1]
dp[0][2]=apts[0][2]
for i in range(0,N-1): #3개 다 선택
        dp[i+1][0]=min(dp[i][1]+apts[i+1][0],dp[i][2]+apts[i+1][0])
        dp[i+1][1]=min(dp[i][0]+apts[i+1][1],dp[i][2]+apts[i+1][1])
        dp[i+1][2]=min(dp[i][1]+apts[i+1][2],dp[i][0]+apts[i+1][2])
print(min(dp[N-1]))
