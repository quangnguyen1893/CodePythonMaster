import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file
file_path = "D:/Master/Master-Code/CodePythonMaster/6 TrucQuanDuLieu/Bai1/data/iris.data"

data = pd.read_csv(file_path, header=None)
# print(data)

# Chọn cột đầu tiên (sepal length) để vẽ histogram
sepal_length_column = data[1]

# Vẽ histogram
plt.hist(sepal_length_column, bins=10, edgecolor='black')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.title('Histogram of Sepal Length')
plt.show()