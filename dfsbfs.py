import sys
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

#Graph 클래스의 인스턴스를 생성할 때 __init__ 메소드가 호출되어 self.graph를 빈 딕셔너리로 초기화합니다.
# 이렇게 함으로써 Graph 객체는 그래프의 모든 노드와 각 노드의 인접 리스트를 저장할 준비가 됩니다.

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
        if v in self.graph:
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]


        #이거 없어도 bfs dfs 맞는데 출력 형식에는 작은게 먼저 선택 된 경우라 이렇게 함. 받을때마다 정렬
        self.graph[u].sort()
        self.graph[v].sort()

# 예제 그래프 생성
g = Graph()
listnum= list(map(int, sys.stdin.readline().split()))
for _ in range(listnum[1]):
    edge=list(map(int, sys.stdin.readline().split()))
    g.add_edge(edge[0],edge[1])



def bfs(graph, start):
    visited = set()
    queue = deque([start])

    #popleft(): deque의 메소드로, 큐의 맨 앞에서 요소를 제거하고 반환합니다
    #vertex: 큐에서 꺼낸 현재 탐색할 노드를 저장하는 변수
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')

            # 인접 노드 중 방문하지 않은 노드를 큐에 추가
            for node in graph[vertex]:
                if node not in visited:
                    queue.append(node)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set() #중복을 허용하지 않는 set 을 사용해 넣어줌


    visited.add(start)
    print(start, end=' ')

    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)


# DFS 실행

dfs(g.graph, listnum[2])
print()
# BFS 실행

bfs(g.graph, listnum[2])
