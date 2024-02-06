#하나를 기준으로 dfs 그리고 다음 실행시 visited 는 앞서 했던 문양에 포함되면 처리.
import sys




N, M = (map(int, sys.stdin.readline().split()))

board = []
visited = [[0] * M for _ in range(N)]
ans=0


for i in range(N):
    row = list(sys.stdin.readline().strip())
    board.append(row)




def testM(Ntile, Mtile):
    next=Mtile+1
    while next<M:
        if board[Ntile][next]=='-':
            visited[Ntile][next]=1
            next+=1
        else:
            break

def testN(Ntile, Mtile):
    next=Ntile+1
    while next<N:
        if board[next][Mtile]=='|':
            visited[next][Mtile]=1
            next+=1
        else:
            break



for i in range(N):
    for k in range(M):
        if visited[i][k]==0 and  board[i][k]=='-':

            testM(i,k)
            ans+=1
        elif  visited[i][k]==0 and  board[i][k]=='|':

            testN(i,k)
            ans+=1

print(ans)


