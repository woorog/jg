import sys
N,tc=map(int, sys.stdin.readline().split())
G = [[] for _ in range(N + 1)]

for _ in range(tc):
    u, v, w = map(int, sys.stdin.readline().split())  # 간선 정보 입력 받기
    G[u].append([v,w])  # 정점 u에서 정점 v로 가는 가중치 w의 간선 추가
    G[v].append([u,w])  # 무방향 그래프이므로, v에서 u로도 동일하게 추가

print(G)