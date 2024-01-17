import heapq
import sys
from collections import deque

# a = list(map(int, sys.stdin.readline().split()))
# a = [1, 2, 3, 4, 5]
#



# 여러 문장.
# n = input()
# a = [sys.stdin.readline() for i in range(n)]
# a = ["1 2 3", "4 5 6"]

# 앞으로의 코딩 입력 방식. dd


# listnum= list(map(int, sys.stdin.readline().split())) 한줄에 입력받는법
# listnum = [int(sys.stdin.readline().strip()) for _ in range(9)]   백준식 입력받기... 이게 하나씩됨
# num = int(sys.stdin.readline()) 한개만
# temp = sys.stdin.readline().split() 종류가 다른것도
#direction_changes = dict(sys.stdin.readline().split() for _ in range(l))
# 키 값 딕셔너러리로 받는법.

from heapq import *

num = int(sys.stdin.readline())
listnum = [int(sys.stdin.readline().strip()) for _ in range(num)]
heap=[]

for i in range(num):
    if listnum[i]==0:
        if len(heap)==0:
            print(0)
        else:
            smallest = heapq.heappop(heap)
            print(smallest)
    else:
        heappush(heap,listnum[i])





#
# print(popnum)