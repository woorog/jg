import sys
from collections import deque

def topological_sort(n, comparisons):
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    # 그래프와 진입 차수 초기화
    for a, b in comparisons:
        graph[a].append(b)
        indegree[b] += 1

    # 진입 차수가 0인 노드를 큐에 삽입
    queue = deque([i for i in range(1, n + 1) if indegree[i] == 0])

    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        # 해당 노드와 연결된 노드들의 진입 차수 감소
        for next_node in graph[node]:
            indegree[next_node] -= 1
            # 새롭게 진입 차수가 0이 된 노드를 큐에 삽입
            if indegree[next_node] == 0:
                queue.append(next_node)

    return result

# 예제 입력
# 예제 입력
n, m = map(int, sys.stdin.readline().split())
comparisons = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]


# 위상 정렬 실행
order = topological_sort(n, comparisons)
print(" ".join(map(str, order)))
