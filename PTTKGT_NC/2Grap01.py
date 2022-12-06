from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True
        count = 0
        while queue:
            s = queue.pop(0)
            count += 1
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return count

n,m = input().split()
g = Graph()
for i in range(int(m)):
    x,y = input().split()
    g.addEdge(int(x), int(y))
h = int(input())
print(int(n) - g.BFS(h))