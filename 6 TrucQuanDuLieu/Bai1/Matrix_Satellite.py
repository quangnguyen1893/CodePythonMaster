import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file
file_path = "D:/Master/Master-Code/CodePythonMaster/6 TrucQuanDuLieu/Bai1/data/sat.trn"
# file_path = "D:/Master/Master-Code/CodePythonMaster/6 TrucQuanDuLieu/Bai1/data/sat.tst"
data = pd.read_csv(file_path, header=None, delimiter=' ')

# Tạo ma trận scatter plot
num_columns = data.shape[1]
fig, axes = plt.subplots(nrows=num_columns, ncols=num_columns, figsize=(15, 15))  # Điều chỉnh kích thước

for i in range(num_columns):
    for j in range(num_columns):
        if i == j:
            axes[i, j].hist(data.iloc[:, i], bins=10, color='blue', alpha=0.7)
        else:
            axes[i, j].scatter(data.iloc[:, i], data.iloc[:, j], c='blue', marker='o', alpha=0.7)
        if i == num_columns - 1:
            axes[i, j].set_xlabel(data.columns[j])
        if j == 0:
            axes[i, j].set_ylabel(data.columns[i])

plt.tight_layout()
plt.show()
