import sys

N=int(sys.stdin.readline())
listnum = [int(sys.stdin.readline().strip()) for _ in range(N)]
listnum.append(0)
nodp=[0]*(N+1)
onedp=[0]*(N+1)
twodp=[0]*(N+1)

onedp[0]=listnum[0]

for i in range(N):
    nodp[i+1]=max(twodp[i],onedp[i],nodp[i])
    onedp[i+1]=nodp[i]+listnum[i+1]
    twodp[i+1]=onedp[i]+listnum[i+1]


print(max(twodp[N-1],onedp[N-1],nodp[N-1]))


listnum=sys.stdin.readline()