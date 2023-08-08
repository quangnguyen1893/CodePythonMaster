import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file
file_path = "D:/Master/Master-Code/CodePythonMaster/6 TrucQuanDuLieu/Bai1/data/segment.data"
with open(file_path, 'r') as f:
    lines = f.readlines()

# Chuyển dữ liệu thành danh sách các dòng
data_lines = [line.strip().split() for line in lines]

# Chuyển dữ liệu thành DataFrame
df = pd.DataFrame(data_lines)

# Chuyển dữ liệu thành kiểu số
df = df.apply(pd.to_numeric)

# Chuẩn hóa dữ liệu bằng Positive Transformation cho dữ liệu âm
# df = df.applymap(lambda x: x + abs(df.min().min()) if x < 0 else x)

# Chuẩn hóa dữ liệu bằng: Min-Max Scaling cho dữ liệu âm
# min_value = df.min().min()
# max_value = df.max().max()
# df = (df - min_value) / (max_value - min_value)

# Chuẩn hóa dữ liệu bằng: Z-Score Standardization cho dữ liệu ==> vẫn còn dữ liệu âm, nên không dùng được
# mean = df.mean()
# std = df.std()
# df = (df - mean) / std

# Chuẩn hóa dữ liệu bằng: Điều chỉnh giá trị tối thiểu cho dữ liệu âm
min_value = df.min().min()
df[df < 0] = df[df < 0] - min_value

# Tính tổng của mỗi cột
column_sums = df.sum()

# Vẽ pie chart
plt.pie(column_sums, labels=df.columns, autopct='%1.1f%%', startangle=140)

# Đặt tiêu đề cho biểu đồ
plt.title('Pie Chart of Data')

# Hiển thị biểu đồ
plt.show()
