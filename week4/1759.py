import sys

tc,m=(map(int,sys.stdin.readline().split()))

reverse=[]
for i in range(tc):
    a,b=(map(int,sys.stdin.readline().split()))
    if a>b:
        reverse.append([b,a])


reverse.sort(key=lambda x:x[0])

start=reverse[0][0]
end=reverse[0][1]
sums=0

for ns,ne in reverse:
    if ns>end:
        sums+=(end-start)*2
        start=ns
        end=ne
    elif ne>end:
        end=ne
    elif ns<start:
        start=ns
sums+=(end-start)*2

print(sums+m)
