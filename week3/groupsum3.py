import sys

num = int(sys.stdin.readline())
numlist = list(map(int, sys.stdin.readline().split()))

ans = numlist[0]
dp = numlist[0]

for i in range(1, num):
    now = numlist[i]
    dp+= now  #더해서 넣기

    if dp < now:  # 현재랑 과거랑 비교해서 크면 dp에 넣어주기
        dp= now
    if ans < dp: #답이랑 지금넣은거 비교해서 크면 답으로 설정
        ans = dp


print(ans)
