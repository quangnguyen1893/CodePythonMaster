import random

# Số đỉnh của đồ thị
num_vertices = 64

# Tạo ma trận đồ thị không liên kết với giá trị ban đầu là 9999999
graph_matrix = [[9999999] * num_vertices for _ in range(num_vertices)]

# Tạo các trọng số ngẫu nhiên và thêm cạnh vào đồ thị
for i in range(num_vertices):
    for j in range(i + 1, num_vertices):
        # Kiểm tra xem có nên thêm cạnh hay không (sử dụng ngẫu nhiên)
        if random.random() < 0.5:
            weight = random.randint(1, 100) 
            graph_matrix[i][j] = weight
            graph_matrix[j][i] = weight

with open("input64.txt", "w") as file:
    for row in graph_matrix:
        file.write(" ".join(map(str, row)) + "\n")
