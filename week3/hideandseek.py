import sys
from collections import deque

S, E = (map(int, sys.stdin.readline().split()))
def find(N, K):
    if N >= K:
        return N - K, 1, [i for i in range(N, K-1, -1)]  # 수빈이가 동생보다 앞에 있거나 같은 위치에 있을 때

    visited = [0] * 100001
    ways = [0] * 100001
    prev = [-1] * 100001  # 이전 위치를 기록하는 배열
    q = deque()
    q.append(N)
    visited[N] = 1
    ways[N] = 1

    while q:
        x = q.popleft()

        for nx in [x - 1, x + 1, x * 2]:
            if 0 <= nx <= 100000:
                if visited[nx] == 0:
                    visited[nx] = visited[x] + 1
                    ways[nx] = ways[x]
                    prev[nx] = x  # 이전 위치 기록
                    q.append(nx)
                elif visited[nx] == visited[x] + 1:
                    ways[nx] += ways[x]

    # 역추적을 통한 경로 구성
    path = []
    current = K
    while current != -1:
        path.append(current)
        current = prev[current]
    path.reverse()

    return visited[K] - 1, ways[K], path

# 예시 입력

fastest_time, num_ways,path = find(S, E)
print(fastest_time)  # 가장 빠른 시간
for i in path:
    print(i,end=' ')

# x=q.popleft()
# print(x)
#
# if 2*x==E or x-1==E or x+1==E:
#     cnt+=1
#     print('b')
#     break
# print( vistied[2*x])
# if vistied[2*x]==0 and 2*x<E+1:
#     vistied[2*x]=1
#     q.append(2*x)
#
# if vistied[x+1]==0 and x+1<E:
#     q.append(x+1)
#     vistied[x+1]=1
#
# if vistied[x-1]==0 and x-1<E:
#     q.append(x-1)
#     vistied[2*1]=1
#
# cnt+=1

#원래 코드랑 다른점은 큐를 다 뽑아서 카운트