import matplotlib.pyplot as plt
import numpy as np

# Đọc dữ liệu từ file
labels = []
data_array = [[] for _ in range(36)]

with open('sat.trn', 'r') as file:
    for line in file:
        values = list(map(float, line.strip().split()))
        for i, value in enumerate(values[:-1]):
            data_array[i].append(value)

# Tạo biểu đồ boxplot
for i, column in enumerate(data_array, start=1):
    max_value = max(column)
    min_value = min(column)
    print(f"Column {i}: Max = {max_value}, Min = {min_value}")

data = [data_array[0], data_array[1], data_array[2], data_array[3], data_array[4], data_array[5], data_array[6], data_array[7], data_array[8], data_array[9], data_array[10], data_array[11], data_array[12], data_array[13], data_array[14], data_array[15], data_array[16], data_array[17], data_array[18], data_array[19], data_array[20], data_array[21], data_array[22], data_array[23], data_array[24], data_array[25], data_array[26], data_array[27], data_array[28], data_array[29], data_array[30], data_array[31], data_array[32], data_array[33], data_array[34], data_array[35]]

fig, ax = plt.subplots(nrows= 1, ncols= 1, figsize=(15, 8))
ax.boxplot(data, flierprops={'marker': 'o', 'markersize': 4, 'markerfacecolor': 'fuchsia'})
#ax.boxplot(data_array[3])
ax.set_title('Boxplot of Data Satellite Image')
ax.set_xlabel('Cột')
ax.set_ylabel('Giá trị')
plt.show()
