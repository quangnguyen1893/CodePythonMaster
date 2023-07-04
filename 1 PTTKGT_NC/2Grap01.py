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

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def DFS(adj, visited, u):
    visited[u] = 1
    for i in range(len(adj[u])):
        if visited[adj[u][i]] == 0:
            DFS(adj, visited, adj[u][i])

def getCount(adj, V, start):
    count = 0
    visited = [0 for i in range(V)]
    DFS(adj, visited, start)

    for u in range(V):
        if visited[u] == 0:
            count += 1
    print(count)

if __name__ == '__main__':
    n, m = input().split()
    adj = [[] for i in range(int(n))]
    for i in range(int(m)):
        x, y = input().split()
        addEdge(adj, int(x)-1, int(y)-1)
    h = int(input())
    getCount(adj, int(n), h-1)