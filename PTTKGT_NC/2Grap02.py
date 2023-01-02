# Có n hòn đảo được đánh số từ 1 đến n. Một số cặp đảo được đánh nối với nhau bằng các cây cầu 2 chiều.
# Minh Minh đứng ở hòn đảo thứ 1 và cô ấy muốn đi đến hòn đảo thứ n. Tính số lượng cây cầu ít nhất mà cô ấy cần phải đi qua để có thể đến được đảo thứ n.
# Đầu vào:
# Dòng đầu tiên là T, số lượng test cases.
# Dòng đầu tiên của mỗi test case là 2 số nguyên n, m cách nhau khoảng trắng - số lượng đảo và tổng số cây cầu.
# m dòng kế tiếp, mỗi dòng là cặp số nguyên x, y cách nhau khoảng trắng - có cầu nối giữa đão và đảo y.
# Đầu ra:
# Mỗi test case được in trên 1 dòng là một số nguyên là số lượng cây cầu ít nhất cần tìm
# Chú ý:
# Bạn có thể an tâm rằng dữ liệu đầu vào luôn hợp lệ
# Ràng buộc
# T=10
# 1 <= n <= 104
# 1 <= m <=  105
# 1 <= x,y <= n
# Python 3 program for the above approach

def add_edge(adj, src, dest):
   adj[src].append(dest)
   adj[dest].append(src)


def BFS(adj, src, dest, v, pred, dist):
   queue = []
   visited = [False for i in range(v)]
   for i in range(v):
      dist[i] = 1000000
      pred[i] = -1
   visited[src] = True
   dist[src] = 0
   queue.append(src)

   while (len(queue) != 0):
      u = queue[0]
      queue.pop(0)
      for i in range(len(adj[u])):
         if (visited[adj[u][i]] == False):
            visited[adj[u][i]] = True
            dist[adj[u][i]] = dist[u] + 1
            pred[adj[u][i]] = u
            queue.append(adj[u][i])
            if (adj[u][i] == dest):
               return True
   return False


def printShortestDistance(adj, s, dest, v):
   pred = [0 for i in range(v)]
   dist = [0 for i in range(v)]
   if (BFS(adj, s, dest, v, pred, dist) == False):
      print("None")
   path = []
   crawl = dest
   path.append(crawl)

   while (pred[crawl] != -1):
      path.append(pred[crawl])
      crawl = pred[crawl]
   print(str(dist[dest]))


if __name__ == '__main__':
   T = int(input())
   for i in range(T):
      n, m = input().split()
      adj = [[] for i in range(int(n))]
      for j in range(int(m)):
         x, y = input().split()
         add_edge(adj, int(x) - 1, int(y) - 1)
      printShortestDistance(adj, 0, int(n) - 1, int(n))