import matplotlib.pyplot as plt
import numpy as np

# Đọc dữ liệu từ file
labels = []
data_array = [[] for _ in range(4)]

with open('iris.data', 'r') as file:
    for line in file:
        values = list(line.strip().split(","))
        for i, value in enumerate(values[:-1]):
            data_array[i].append(float(value))

# Tạo biểu đồ boxplot
for i, column in enumerate(data_array, start=1):
    max_value = max(column)
    min_value = min(column)
    print(f"Column {i}: Max = {max_value}, Min = {min_value}")

data = [data_array[0], data_array[1], data_array[2], data_array[3]]

fig, ax = plt.subplots(nrows= 1, ncols= 1, figsize=(15, 8))
ax.boxplot(data, flierprops={'marker': 'o', 'markersize': 4, 'markerfacecolor': 'fuchsia'})
#ax.boxplot(data_array[3])
ax.set_title('Boxplot of Data Iris')
ax.set_xlabel('Cột')
ax.set_ylabel('Giá trị')
plt.show()
