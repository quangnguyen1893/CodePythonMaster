import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

# Đọc dữ liệu từ file văn bản
file_path = "D:/Master/Master-Code/CodePythonMaster/6 TrucQuanDuLieu/Bai1/data/iris.data"
data = pd.read_csv(file_path, header=None)

# Xác định tên cột và dữ liệu
column_names = data.columns.tolist()
class_column = column_names[-1]  # Giả định cột cuối cùng là cột chứa tên lớp
feature_columns = column_names[:-1]  # Các cột trước đó là các cột dữ liệu đặc trưng

# Vẽ biểu đồ Parallel Coordinate
plt.figure(figsize=(10, 6))
parallel_coordinates(data, class_column, color=['r', 'g', 'b'])
plt.title('Parallel Coordinate Plot of Iris Classes')
plt.show()
