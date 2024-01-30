import sys

tc=int(sys.stdin.readline())

stack=[0]*21

for i in range(tc):
    strr=list(map(str, sys.stdin.readline().split()))

    if strr[0]=='add':
        stack[int(strr[1])]=1
    elif strr[0]=='remove':
        stack[int(strr[1])]=0
    elif strr[0]=='check':
        if stack[int(strr[1])]==1:
            print(1)
        else:
            print(0)
    elif strr[0]=='toggle':
        if stack[int(strr[1])]==0:
            stack[int(strr[1])]=1
        else:
            stack[int(strr[1])]=0
    elif strr[0]=='all':
        stack=[1]*21
    elif strr[0]=='empty':
        stack=[0]*21
