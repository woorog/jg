# a = list(map(int, sys.stdin.readline().split()))
# a = [1, 2, 3, 4, 5]
#

# 문자열 내장 함수 코딩테스트를 위한 Python 정리
# ▶ lower ▶ upper ▶ find ▶ count
#
# 리스트 내장함수
# append
# insert
# a.insert(i, v) : i번 인덱스에 v 추가
# pop
# a.pop() : 마지막 원소 꺼내기 (꺼낸 값 반환)
# a.pop(i) : i번 인덱스 값 꺼내기 (꺼낸 값 반환)
# remove
#  a.remove(v) : v 값을 찾아서 제거
# index
# a.index(v) : v가 리스트의 몇 번째 index에 있는지 반환
# ord( ) / chr( )
# ord()는 문자열을 아스키코드(숫자)로 반환하는 함수이고, chr()은 아스키코드를 문자열로 반환하는 함수!
# isalpha( ) / isalnum( )
# isalpha()는 문자열이면 True, 아니면 False를 리턴하고,
# isalnum()은 숫자면 True, 아니면 False를 리턴함

# 여러 문장.
# n = input()
# a = [sys.stdin.readline() for i in range(n)]
# a = ["1 2 3", "4 5 6"]

# 앞으로의 코딩 입력 방식. dd

#M, N, H = (map(int, sys.stdin.readline().split()))
# listnum= list(map(int, sys.stdin.readline().split())) 한줄에 입력받는법
# listnum = [int(sys.stdin.readline().strip()) for _ in range(9)]   백준식 입력받기... 이게 하나씩됨
# num = int(sys.stdin.readline()) 한개만
# temp = sys.stdin.readline().split() 종류가 다른것도
# direction_changes = dict(sys.stdin.readline().split() for _ in range(l))
# 키 값 딕셔너러리로 받는법.
# product()
# p, q, … [repeat=1]
# 데카르트 곱(cartesian product), 중첩된 for 루프와 동등합니다
# permutations()
# p[, r]
# r-길이 튜플들, 모든 가능한 순서, 반복되는 요소 없음
# combinations()
# p, r
# r-길이 튜플들, 정렬된 순서, 반복되는 요소 없음
#
# heapq 사용법  heapq.heappop(heap) heappush(heap,12)

from itertools import *
import sys
num = []

listp=["x","/","%"]

printList = list(product(*listp))
print(printList)

# for sumlist in printList:
#     ans = []
#     if sum(sumlist) == 100:
#         ans = sorted(sumlist)
#         for i in ans:
#             print(i)
#         break



