import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# Đọc dữ liệu từ tệp
with open('segment.data', 'r') as file:
    data = file.readlines()

# Chia khoảng giá trị
value_ranges = np.arange(0, 20, 1)  #

# Tạo một từ điển để lưu trữ dữ liệu theo lớp và khoảng giá trị
class_range_data = defaultdict(lambda: {r: 0 for r in value_ranges})
for line in data:
    parts = list(line.strip().split())
    class_label = parts[-1]
    values = parts[:-1]
    
    for value in values:
        for r in value_ranges:
            if float(value) <= r:
                class_range_data[class_label][r] += 1
                break

# Vẽ histogram cho nhiều lớp trên cùng một biểu đồ
plt.figure(figsize=(10, 6))  # Kích thước biểu đồ

for class_label, range_data in class_range_data.items():
    plt.bar(range_data.keys(), range_data.values(), width=8, align='center', label=f'Lớp {class_label}')

plt.xlabel('Giá trị')
plt.ylabel('Tần suất')
plt.title('Histogram tập dữ liệu Segment')
plt.legend()
plt.grid(True)
plt.show()
