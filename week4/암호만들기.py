import sys
import itertools

N, H = (map(int, sys.stdin.readline().split()))

alist=list(map(str,sys.stdin.readline().split()))

alist=sorted(alist)

combi=(list(itertools.combinations(alist,N)))
<<<<<<< HEAD

=======
>>>>>>> origin/test
ans=[]
realans=[]
for i in combi:
    for k in i:
        if k=='a' or k=='e' or k=='i' or k=='o' or k=='u':
            ans.append(i)
            break

for i in ans:
    cnt=0
    for k in i:
        if k=='a' or k=='e' or k=='i' or k=='o' or k=='u':
            continue
        else:
            cnt+=1
    if cnt>=2:
        realans.append(i)


for i in realans:
    print("".join(i))
