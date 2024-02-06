import sys

num=int(sys.stdin.readline())
lists=[]

for _ in range(num):
    lists.append(list(map(int,sys.stdin.readline().split())))






dp=[0]*(100)
for i in range(num):
    x,y=lists[i][0]-1,lists[i][1]-1
    if x>=y:
        for k in range(y,x):
            dp[k]+=1
    else:
        for k in range(x,y):
            dp[k]+=1
print(dp)
print(max(dp))