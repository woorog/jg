import sys

N,M = (map(int, sys.stdin.readline().split()))

board=[]
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

print(board)