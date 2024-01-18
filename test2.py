



class graph:
    def __init__(self):
        self.graph={}

#self가 없을 때:
    def __str__(self):
        return str(self.graph)
#만약 이 메서드에서 self를 사용하지 않으면,
# graph는 로컬 변수로 간주되고 클래스의 인스턴스 변수인 graph에 접근할 수 없습니다.
    def insert_edge(self,n,m):
        if n in self.graph:
            self.graph[n].append(m)
        else:
            self.graph[n]=[m]
        if m in self.graph:
            self.graph[m].append(n)
        else:
            self.graph[m]=[n]






g=graph()

g.insert_edge(1,2)
g.insert_edge(1,3)
g.insert_edge(1,4)
g.insert_edge(2,5)

print(g)





