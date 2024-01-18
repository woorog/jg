# a = list(map(int, sys.stdin.readline().split()))
# a = [1, 2, 3, 4, 5]
#

# 문자열 내장 함수 코딩테스트를 위한 Python 정리
# ▶ lower ▶ upper ▶ find ▶ count
#
# 리스트 내장함수
# append
# insert
# a.insert(i, v) : i번 인덱스에 v 추가
# pop
# a.pop() : 마지막 원소 꺼내기 (꺼낸 값 반환)
# a.pop(i) : i번 인덱스 값 꺼내기 (꺼낸 값 반환)
# remove
#  a.remove(v) : v 값을 찾아서 제거
# index
# a.index(v) : v가 리스트의 몇 번째 index에 있는지 반환
# ord( ) / chr( )
# ord()는 문자열을 아스키코드(숫자)로 반환하는 함수이고, chr()은 아스키코드를 문자열로 반환하는 함수!
# isalpha( ) / isalnum( )
# isalpha()는 문자열이면 True, 아니면 False를 리턴하고,
# isalnum()은 숫자면 True, 아니면 False를 리턴함

# 여러 문장.
# n = input()
# a = [sys.stdin.readline() for i in range(n)]
# a = ["1 2 3", "4 5 6"]

# 앞으로의 코딩 입력 방식. dd


# listnum= list(map(int, sys.stdin.readline().split())) 한줄에 입력받는법
# listnum = [int(sys.stdin.readline().strip()) for _ in range(9)]   백준식 입력받기... 이게 하나씩됨
# num = int(sys.stdin.readline()) 한개만
# temp = sys.stdin.readline().split() 종류가 다른것도
# direction_changes = dict(sys.stdin.readline().split() for _ in range(l))
# 키 값 딕셔너러리로 받는법.
# product()
# p, q, … [repeat=1]
# 데카르트 곱(cartesian product), 중첩된 for 루프와 동등합니다
# permutations()
# p[, r]
# r-길이 튜플들, 모든 가능한 순서, 반복되는 요소 없음
# combinations()
# p, r
# r-길이 튜플들, 정렬된 순서, 반복되는 요소 없음
#
# heapq 사용법  heapq.heappop(heap) heappush(heap,12)

import  sys

class Graph:
    def __init__(self):
        self.graph = {}

    #이 부분이 출력을 위해 문자열로 반환 시키는 함수
    def __str__(self):
        return str(self.graph)

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


        # #이거 없어도 bfs dfs 맞는데 출력 형식에는 작은게 먼저 선택 된 경우라 이렇게 함. 받을때마다 정렬
        # self.graph[u].sort()
        # self.graph[v].sort()

# 예제 그래프 생성
g = Graph()

listnum= list(map(int, sys.stdin.readline().split()))
for _ in range(listnum[1]):
    edge=list(map(int, sys.stdin.readline().split()))
    g.add_edge(edge[0],edge[1])


# 왜 그냥 출력이 안되는가?
#정수로만 구성된 입력을 받는다고 해도, Graph 클래스의 인스턴스를 print 함수로 출력할 때는
# 해당 인스턴스를 어떻게 문자열로 표현할지 정의해야 합니다. Python에서 객체를 문자열로 출력하려면,
# 객체가 문자열 표현을 제공해야 하며, 이는 __str__ 또는 __repr__ 매직 메소드를 구현함으로써 가능합니다.

print(g)


