import sys


class Graph:
    def __init__(self, num_vertices):
        self.graph = {i: [] for i in range(1, num_vertices + 1)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start, visited, kill):
        if start in kill:
            return True
        visited.add(start)
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                if self.dfs(neighbor, visited, kill):
                    return True
        return False




N, tc = (map(int, sys.stdin.readline().split()))

kill=list(map(int, sys.stdin.readline().split()))
kill.pop(0)
member=[]
for _ in range(tc):
    member.append(list(map(int, sys.stdin.readline().split())))

for i in range(tc):
    member[i].pop(0)
#맴버의 0번은 제외하고 1번부터 찾을거임
#요소가 3개이상인 멤버들을 기준으로 간선 이어줄거임 확인은 마지막에.


g = Graph(N)
count = 0

# 멤버 그룹 간의 간선 추가
for member_group in member:
    for i in range(len(member_group) - 1):
        for j in range(i + 1, len(member_group)):
            g.add_edge(member_group[i], member_group[j])


for member_group in member:
    if len(member_group) < 2:
        continue
    visited = set()  # DFS 탐색을 위한 방문한 노드 집합
    for member_id in member_group:
        # DFS로 멤버의 그래프 연결 탐색
        if g.dfs(member_id, visited, kill):
            count += 1
            break  # kill 리스트의 요소를 발견하면 이 멤버 그룹에 대한 탐색 중단

print(tc-count)



