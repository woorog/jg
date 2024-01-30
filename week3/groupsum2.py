import sys

N,tc=map(int, sys.stdin.readline().split())
numlist=[]
for _ in range(N):
    numlist.append(list(map(int, sys.stdin.readline().split())))

print(numlist)
cumulative_sum = [[] for _ in range(N)]


for i in range(N):
    current_sum = 0
    for num in numlist[i]:
        current_sum += num
        cumulative_sum[i].append(current_sum)

print(cumulative_sum)


for _ in range(tc):
    S_x,S_y,E_x,E_y=(map(int, sys.stdin.readline().split()))
    print(S_x,S_y,E_x,E_y)
    if S_x==E_x and S_y==E_y: #좌표가 같을때 둘중에 하나 그냥 출력
        print(numlist[S_x][S_y])
    elif S_x<E_x and S_y==E_y: # y 좌표가 같을때
        print()
    elif S_y<E_y and S_x==E_x: # x 좌표만 같으면 y값 다 더해주면 됨
        print()
    else:  #그냥 다를 경우.
        print()

    # S_index-=1
    # E_index-=1
    #
    # if S_index==E_index:
    #     range_sum=numlist[S_index]
    # elif S_index == 0:
    #     range_sum = cumulative_sum[E_index]
    # else:
    #     range_sum = cumulative_sum[E_index] - cumulative_sum[S_index - 1]

    # print(range_sum)

