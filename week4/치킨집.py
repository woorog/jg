import sys
from itertools import combinations

MM,N=map(int, sys.stdin.readline().split())

clist=[]
hlist=[]
Maps=[]
for _ in range(MM):
    Maps.append(list(map(int,sys.stdin.readline().split())))


for i in range(MM):
    for l in range(MM):
        if Maps[i][l]==2:
            clist.append((i,l))
        elif Maps[i][l]==1:
            hlist.append((i,l))

allcombo=[]
if N==1:
    allcombo=clist
else:
    for i in combinations(clist, N):
        allcombo.append(i)
# print(allcombo)
# print(hlist)
# print(clist)
ans=9999
if N==1:
    for a,b in clist:
        now=999
        temp=0
        for home1,home2 in hlist:
            temp+=(abs(a-home1)+abs(b-home2))
        if temp<ans:
            ans=temp
else:
    for k in allcombo:
        now=999
        numlist=[9999]*len(hlist)
        for a,b in k:
            c=0
            for home1,home2 in hlist:
                temp=(abs(a-home1)+abs(b-home2))
                if numlist[c]>temp:
                    numlist[c]=temp
                c+=1
        tempans=sum(numlist)
        if tempans<ans:
            ans=tempans

print(ans)