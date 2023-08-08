import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Đọc dữ liệu từ file
file_path = "D:/Master/Master-Code/CodePythonMaster/6 TrucQuanDuLieu/Bai1/data/iris.data"
data = pd.read_csv(file_path, header=None)

# Đặt tên cột cho dữ liệu
column_names = [f'Feature_{i}' for i in range(data.shape[1])]
data.columns = column_names

# Chia tên cột và dữ liệu
features = data.iloc[:, :-1]
labels = data.iloc[:, -1]

# Tạo Starglyph Plot
fig = plt.figure(figsize=(10, 10))  # Tăng kích thước biểu đồ
ax = plt.subplot(111, polar=True)

# Tính số lượng feature
num_features = len(features.columns)

# Tính góc cho mỗi feature
angles = np.linspace(0, 2 * np.pi, num_features, endpoint=False)

# Thêm feature đầu tiên vào cuối danh sách để đóng vòng tròn
features = pd.concat([features, features[features.columns[0]]], axis=1)

# Màu sắc cho từng loại dữ liệu
colors = plt.cm.viridis(np.linspace(0, 1, len(labels)))

# Vẽ các đường thẳng nối các điểm dữ liệu
for i, row in enumerate(features.iterrows()):
    values = row[1].values[:-1]  # Loại bỏ cột cuối vì đó là label
    ax.plot(angles, values, label=labels[i], color=colors[i])
    ax.fill(angles, values, alpha=0.25, color=colors[i])

# Đặt góc cho mỗi feature
ax.set_xticks(angles)
ax.set_xticklabels(features.columns[:-1])  # Loại bỏ cột cuối

# Đặt độ lớn cho trục y
ax.set_rlabel_position(0)
plt.yticks([])

# Đặt tiêu đề cho biểu đồ
plt.title('Starglyph Plot')

# Hiển thị legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Hiển thị biểu đồ
plt.show()
