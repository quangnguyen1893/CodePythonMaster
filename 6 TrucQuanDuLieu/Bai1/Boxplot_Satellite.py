import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file
# file_path = "D:/Master/Master-Code/CodePythonMaster/6 TrucQuanDuLieu/Bai1/data/sat.trn"
file_path = "D:/Master/Master-Code/CodePythonMaster/6 TrucQuanDuLieu/Bai1/data/sat.tst"
with open(file_path, 'r') as f:
    lines = f.readlines()

# Chuyển dữ liệu thành danh sách các dòng
data_lines = [line.strip().split() for line in lines]

# Chuyển dữ liệu thành DataFrame
df = pd.DataFrame(data_lines)

# Chuyển dữ liệu thành kiểu số
df = df.apply(pd.to_numeric)

# Vẽ box plot
df.plot(kind='box')

# Đặt tiêu đề cho biểu đồ
plt.title('Box Plot of Data')

# Hiển thị biểu đồ
plt.show()
