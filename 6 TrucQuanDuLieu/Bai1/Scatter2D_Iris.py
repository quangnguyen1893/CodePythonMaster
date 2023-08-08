import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file
file_path = "D:/Master/Master-Code/CodePythonMaster/6 TrucQuanDuLieu/Bai1/data/iris.data"
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
df = pd.read_csv(file_path, names=column_names)

# Tách dữ liệu vào các cột riêng biệt
sepal_length = df["sepal_length"]
sepal_width = df["sepal_width"]
species = df["species"]

# Tạo scatter plot
plt.figure(figsize=(10, 6))  # Đặt kích thước biểu đồ
plt.scatter(sepal_length, sepal_width, c='blue', marker='o', label='Iris-setosa')

# Đặt tiêu đề và nhãn cho biểu đồ
plt.title('Scatter Plot of Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')

# Hiển thị legend và biểu đồ
plt.legend()
plt.grid(True)
plt.show()
