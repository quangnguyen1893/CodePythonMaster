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
class Graph_structure:
   def __init__(self, V):
      self.V = V
      self.adj = [[] for i in range(V)]

   def DFS_Utility(self, temp, v, visited):
      visited[v] = True
      temp.append(v)
      for i in self.adj[v]:
         if visited[i] == False:
            temp = self.DFS_Utility(temp, i, visited)
      return temp

   def add_edge(self, v, w):
      self.adj[v].append(w)
      self.adj[w].append(v)

   def find_connected_components(self):
      visited = []
      connected_comp = []
      for i in range(self.V):
         visited.append(False)
      for v in range(self.V):
         if visited[v] == False:
            temp = []
            connected_comp.append(self.DFS_Utility(temp, v, visited))
      return connected_comp

my_instance = Graph_structure(6)
my_instance.add_edge(1, 0)
my_instance.add_edge(2, 3)
my_instance.add_edge(3, 4)
my_instance.add_edge(5, 0)
# print("There are 6 edges. They are : ")
# print("1-->0")
# print("2-->3")
# print("3-->4")
# print("5-->0")

connected_comp = my_instance.find_connected_components()
print("The connected components are...")
print(connected_comp)
