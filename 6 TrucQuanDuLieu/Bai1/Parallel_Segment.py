import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

# Đọc dữ liệu từ file
file_path = "D:/Master/Master-Code/CodePythonMaster/6 TrucQuanDuLieu/Bai1/data/segment.data"
data = pd.read_csv(file_path, header=None, delimiter=' ')

# Đặt tên cột cho dữ liệu
column_names = [f'Feature_{i}' for i in range(data.shape[1])]
data.columns = column_names

# Chuẩn hóa dữ liệu giá trị âm
    # Phương pháp "Positive Transformation"
# min_value = data.min().min() # Tìm giá trị tối thiểu trong dữ liệu âm
# data = data + abs(min_value) + 1  # Áp dụng Positive Transformation bằng cộng giá trị tối thiểu; Thêm 1 để tránh giá trị 0

    # Chuẩn hóa dữ liệu bằng: Min-Max Scaling cho dữ liệu âm
# min_value = data.min().min()
# max_value = data.max().max()
# data = (data - min_value) / (max_value - min_value)

    # Áp dụng Z-Score Standardization cho dữ liệu âm
# data = (data - data.mean()) / data.std()

    # Chuẩn hóa dữ liệu bằng: Điều chỉnh giá trị tối thiểu cho dữ liệu âm
min_value = data.min().min() # Tìm giá trị tối thiểu trong dữ liệu âm
adjusted_data = data + abs(min_value) + 1  # Điều chỉnh giá trị tối thiểu cho dữ liệu âm ; Thêm 1 để đảm bảo giá trị sau điều chỉnh dương

# Kết thúc chuẩn hóa

# Hiển thị Parallel Coordinates
plt.figure(figsize=(10, 6))  # Đặt kích thước biểu đồ
parallel_coordinates(data, 'Feature_19', colormap='viridis')

# Đặt tiêu đề cho biểu đồ
plt.title('Parallel Coordinates Plot')

plt.show()
