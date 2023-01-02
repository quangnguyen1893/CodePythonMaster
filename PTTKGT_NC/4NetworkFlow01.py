
import operator
class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def BFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True

        return False

    def FordFulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0
        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

m = int(input())
list = {}
V = {}
for i in range(m):
    row = input().split()
    list[row[0]+row[1]] = int(row[2])
    if row[0] in V:
        V[row[0]]['T'] = 0
    else:
        V[row[0]] = {'T' : 0, 'P' : 1}
    if row[1] in V:
        V[row[1]]['P'] = 0
    else:
        V[row[1]] = {'T' : 1, 'P' : 0}

S = ''
T = ''
D = []
for k, v in V.items():
    # print(v)
    if v['P']:
        S = k
    elif v['T']:
        T = k
    else:
        D.append(k)

D = [S] + D + [T]
# print(D)
graph = []
for d in D:
    t = []
    for dd in D:
        tmp = d + dd
        if tmp in list:
            t.append(list[tmp])
        else:
            t.append(0)
    graph.append(t)

g = Graph(graph)
print(g.FordFulkerson(0, len(D)-1))