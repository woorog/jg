import sys
input = sys.stdin.readline  # 표준 입력을 더 빠르게 받기 위해 sys.stdin.readline 사용
from heapq import heappush, heappop  # 우선순위 큐를 위한 heapq 모듈 사용

def dijkstra(start, end):
    dis = [0xffffff] * (N + 1)  # 최단 거리를 저장할 배열, 초기값은 매우 큰 값(0xffffff)으로 설정
    dis[start] = 0  # 시작 정점의 최단 거리는 0
    q = [[0, start]]  # 우선순위 큐 초기화, (거리, 정점) 형태로 저장
    while q:
        k, u = heappop(q)  # 큐에서 최소 거리 정점 추출
        if k > dis[u]:
            continue  # 현재 거리가 저장된 거리보다 크면 무시

        for w, v in G[u]:
            if dis[v] > dis[u] + w:  # 현재 정점을 거쳐 다른 정점으로 가는 거리가 더 짧은 경우
                dis[v] = dis[u] + w  # 최단 거리 업데이트
                heappush(q, [dis[v], v])  # 업데이트된 거리와 정점을 큐에 추가

    return dis[end]  # 종료 정점까지의 최단 거리 반환

N, E = map(int, input().split())  # 정점의 개수 N, 간선의 개수 E 입력 받기
G = [[] for _ in range(N + 1)]  # 각 정점에서 다른 정점으로 가는 간선과 가중치를 저장할 그래프 G 초기화
for _ in range(E):
    u, v, w = map(int, input().split())  # 간선 정보 입력 받기
    G[u].append([w, v])  # 정점 u에서 정점 v로 가는 가중치 w의 간선 추가
    G[v].append([w, u])  # 무방향 그래프이므로, v에서 u로도 동일하게 추가

stop1, stop2 = map(int, input().split())  # 반드시 거쳐야 하는 두 정점 stop1, stop2 입력 받기

# 1번 정점에서 N번 정점까지 이동하는 두 가지 경로 계산
path1 = dijkstra(1, stop1) + dijkstra(stop1, stop2) + dijkstra(stop2, N)  # 경로 1: 1 -> stop1 -> stop2 -> N
path2 = dijkstra(1, stop2) + dijkstra(stop2, stop1) + dijkstra(stop1, N)  # 경로 2: 1 -> stop2 -> stop1 -> N

# 두 경로 중 하나라도 계산된 최단 거리가 초기값(0xff`ffff)과 같거나 크면, 경로가 없는 것으로 간주하여 -1 출력
if path1 >= 0xffffff and path2 >= 0xffffff:
    print(-1)
else:
    # 두 경로 중 최소값을 출력
    print(min(path1, path2))