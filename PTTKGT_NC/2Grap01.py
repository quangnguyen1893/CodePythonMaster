# Cho đồ thị vô hướng gồm n đỉnh và m cạnh. Bắt đầu tại một đỉnh gọi là head. Tính số lượng đỉnh không thể đi tới được từ head.
#
# Đầu vào
# Dòng đầu tiên của mỗi test case là 2 số nguyên n, m cách nhau khoảng trắng - số lượng đảo và tổng số cây cầu.
# m dòng kế tiếp, mỗi dòng là cặp số nguyên x, y cách nhau khoảng trắng - cạnh vô hướng giữa 2 đỉnh x và y
# Dòng kế tiếp gồm 1 số nguyên gọi là head
#
# Đầu ra
# Một số nguyên là số lượng đỉnh không thể đi tới từ head
#
# Chú ý:
# Bạn có thể an tâm rằng dữ liệu đầu vào luôn hợp lệ
# Ràng buộc
# 1 <= n, m<= 1000
# 1 <= x, y,x <= n

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