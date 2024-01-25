import sys
from collections import deque


def bfs_modified(box):
    queue = deque()
    visited = set()

    for i in (P,M,X,D):
        if i ==0:
            continue
        else:
            while queue:
                z, y, x = queue.popleft()








num=int(sys.stdin.readline())
listnum= list(map(int, sys.stdin.readline().split()))
P, M, X ,D = (map(int, sys.stdin.readline().split()))