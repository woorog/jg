
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

import heapq

import heapq

def find_medians(nums):
    max_heap = []  # 작은 값들을 저장하는 최대 힙
    min_heap = []  # 큰 값들을 저장하는 최소 힙
    result = []

    for num in nums:
        if not max_heap or -max_heap[0] >= num:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        result.append(-max_heap[0])



        # 현재 최대 힙과 최소 힙의 상태를 출력합니다.
        print("Max Heap:", [-x for x in max_heap])  # 최대 힙의 원래 값들
        print("Min Heap:", min_heap)
        print("Current Median:", result[-1])
        print("----------------------")

    return result

# 테스트 데이터
nums = [1, 5, 2, 10, -99, 7,]

medians = find_medians(nums)