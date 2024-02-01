import sys

N,case=map(int, sys.stdin.readline().split())
cards=list(map(int,sys.stdin.readline().split()))

for _ in range(case):
    cards.sort()

    sums=cards[0]+cards[1]

    cards[0]=sums
    cards[1]=sums

print(sum(cards))