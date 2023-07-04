# Có n hòn đảo được đánh số từ 1 đến n. Một số cặp đảo được đánh nối với nhau bằng các cây cầu 1 chiều có thu phí.
# Chi phí để đi qua cây cầu giữa 2 đảo x, y là w.
# Minh Minh đứng ở hòn đảo thứ 1 và cô ấy muốn đi đến hòn đảo thứ n. Tính chi phí thấp nhất để cô ấy có thể đến được hòn đảo thứ n.
# Đầu vào:
# Dòng đầu tiên là 2 số nguyên n, m cách nhau khoảng trắng - số lượng đảo và tổng số cây cầu.
# m dòng kế tiếp, mỗi dòng là 3 số nguyên x, y, w cách nhau khoảng trắng - chi phí đi qua cầu nối giữa 2 đảo x và y là w
# Đầu ra:
# Một số nguyên duy nhất là chi phí thấp nhất cần tìm. Nếu không thể đi được đến đảo n, hiển thị 109
# Chú ý:
# Bạn có thể an tâm rằng dữ liệu đầu vào luôn hợp lệ
# Ràng buộc
# 1 <= n <= 105
# 1 <= m <=  3∗105
# 1 <= x,y <= n
# 1 <= w <= 10000

# Python3 program for Bellman-Ford's single source
# shortest path algorithm.

# Class to represent a graph

from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight

def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0
    pq = PriorityQueue()
    pq.put((0, start_vertex))
    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)
        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


n_m = input().split()
n, m = (int(x) for x in n_m)
g = Graph(n)
count_check = True
while m > 0:
    x_y_w = input().split()
    x, y, w = (int(x) for x in x_y_w)
    g.add_edge(x - 1, y - 1, w)
    m -= 1
if count_check is False:
    print(int(1e9))
else:
    D = dijkstra(g, 0)
    if D[n - 1] == float('inf'):
        print(int(1e9))
    else:
        print(D[n - 1])