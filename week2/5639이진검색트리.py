# 분할 정복 문제.
# 루트값보다 작아지다가 커지는 경우를 구분값으로 하여 왼쪽, 오른쪽을 분할하여 탐색
# 루트값보다 커지기만 하는 경우, 양쪽에 서브 트리가 아예 없는 경우에는 리턴이 없음
import sys

sys.setrecursionlimit(10**6)
import sys
from collections import deque
input = sys.stdin.readline

binary = []

for i in sys.stdin:
    x = i.split('\n')
    binary.append(int(x[0]))

def post_order(start, end, pre_list):
    if start > end:
        return None

    root = pre_list[start]
    point = start+1

    while point <= end:
        if pre_list[point] > root:
            break
        point += 1

    post_order(start+1, point-1, pre_list)
    post_order(point, end, pre_list)

    print(root)

post_order(0, len(binary)-1, binary)