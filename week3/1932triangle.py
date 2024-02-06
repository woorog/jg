import sys

tc=int(sys.stdin.readline())
arr=[]
for i in range(tc):
    arr.append(list(map(int, sys.stdin.readline().split())))

dp=[[0]*(tc+1) for i in range(tc+1)]

dp[0][0]=arr[0][0]

for i in range(tc):
    for k in range(len(arr[i])):
        if i+1<tc and dp[i][k]+arr[i+1][k]>dp[i+1][k] :
            dp[i+1][k]=dp[i][k]+arr[i+1][k]

        if i+1<tc and dp[i][k]+arr[i+1][k+1]>dp[i+1][k+1]:
            dp[i+1][k+1]=dp[i][k]+arr[i+1][k+1]






print(max(dp[tc-1]))
