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
def max_people(n, positions, d):

    max_people = 0


    for i in range(n):
        count = 0
        start_point = positions[i][0]
        end_point = start_point + d


        for hi, oi in positions:
            if start_point <= hi <= end_point and start_point <= oi <= end_point:
                count += 1

        max_people = max(max_people, count)

    return max_people

n = int(sys.stdin.readline())
positions = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
d = int(sys.stdin.readline())


print(max_people(n, positions, d))
