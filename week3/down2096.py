
#
# tc=int(sys.stdin.readline())
# line=[]
# for i in range(tc):
#    line.append(list(map(int,sys.stdin.readline().split())))
#
# line.append([0]*(len(line)))
#
# dp=[[0]*(len(line)-1) for i in range(tc+1)]
# dp[0]=line[0]
# mdp=[[10]*(len(line)-1) for i in range(tc+1)]
# mdp[0]=line[0]
#
# for i in range(tc):
#     for k in range(3):
#         if k==0:
#             dp[i+1][k]=max(dp[i][k]+line[i+1][k],dp[i][k+1]+line[i+1][k])
#             mdp[i+1][k]=min(mdp[i][k]+line[i+1][k],mdp[i][k+1]+line[i+1][k])
#         elif k==1:
#             dp[i+1][k]=max(dp[i][k]+line[i+1][k],dp[i][k+1]+line[i+1][k],dp[i][k-1]+line[i+1][k])
#             mdp[i+1][k]=min(mdp[i][k]+line[i+1][k],mdp[i][k+1]+line[i+1][k],mdp[i][k-1]+line[i+1][k])
#
#         elif k==2:
#             dp[i+1][k]=max(dp[i][k]+line[i+1][k],dp[i][k-1]+line[i+1][k])
#             mdp[i+1][k]=min(mdp[i][k]+line[i+1][k],mdp[i][k-1]+line[i+1][k])
#
#
# print(max(dp[tc]),min(mdp[tc]))
#


# import sys
# read = sys.stdin.readline
#
#
# tc=int(sys.stdin.readline())
# line=[]
# for i in range(tc):
#     line.append(list(map(int,sys.stdin.readline().split())))
#
# line.append([0]*(len(line)))
#
# dp=line[0]
# mdp=line[0]
#
#
#
# for i in range(tc):
#     nmdp=[0,0,0]
#     ndp=[0,0,0]
#
#     for k in range(3):
#         if k==0:
#             ndp[k]=max(dp[k]+line[i+1][k],dp[k+1]+line[i+1][k])
#             nmdp[k]=min(mdp[k]+line[i+1][k],mdp[k+1]+line[i+1][k])
#         if k==1:
#             ndp[k]=max(dp[k]+line[i+1][k],dp[k+1]+line[i+1][k],dp[k-1]+line[i+1][k])
#             nmdp[k]=min(mdp[k]+line[i+1][k],mdp[k+1]+line[i+1][k],mdp[k-1]+line[i+1][k])
#
#         if k==2:
#             ndp[k]=max(dp[k]+line[i+1][k],dp[k-1]+line[i+1][k])
#             nmdp[k]=min(mdp[k]+line[i+1][k],mdp[k-1]+line[i+1][k])
#
#
#     dp=ndp
#     mdp=nmdp
#
#
# print(max(dp),min(mdp))




import sys
read = sys.stdin.readline

tc = int(read())
dp = [0, 0, 0]
mdp = [0, 0, 0]

for _ in range(tc):
    line = list(map(int, read().split()))
    ndp = [0, 0, 0]
    nmdp = [0, 0, 0]

    for k in range(3):
        if k == 0:
            ndp[k] = max(dp[k] + line[k], dp[k + 1] + line[k])
            nmdp[k] = min(mdp[k] + line[k], mdp[k + 1] + line[k])
        elif k == 1:
            ndp[k] = max(dp[k] + line[k], dp[k + 1] + line[k], dp[k - 1] + line[k])
            nmdp[k] = min(mdp[k] + line[k], mdp[k + 1] + line[k], mdp[k - 1] + line[k])
        elif k == 2:
            ndp[k] = max(dp[k] + line[k], dp[k - 1] + line[k])
            nmdp[k] = min(mdp[k] + line[k], mdp[k - 1] + line[k])

    dp, mdp = ndp, nmdp

print(max(dp), min(mdp))
