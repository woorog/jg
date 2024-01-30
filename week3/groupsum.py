import sys

num,tc=map(int, sys.stdin.readline().split())
numlist=list(map(int, sys.stdin.readline().split()))
cumulative_sum = []
current_sum = 0
for num in numlist:
    current_sum += num
    cumulative_sum.append(current_sum)

print(cumulative_sum)

for _ in range(tc):
    sum=0

    S_index,E_index=(map(int, sys.stdin.readline().split()))
    S_index-=1
    E_index-=1

    if S_index==E_index:
        range_sum=numlist[S_index]
    elif S_index == 0:
        range_sum = cumulative_sum[E_index]
    else:
        range_sum = cumulative_sum[E_index] - cumulative_sum[S_index - 1]

    print(range_sum)

