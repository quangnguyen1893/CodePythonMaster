import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tập tin txt
data = []
with open('D:/Master/Master-Code/CodePythonMaster/6 TrucQuanDuLieu/Bai1/data/segment.data', 'r') as file:
    for line in file:
        line = line.strip()
        values = line.split()
        data.append(values)

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Sử dụng cột cuối cùng làm nhãn
labels = df.iloc[:, -1]

# Đếm số lượng mỗi nhãn
rrr = labels.value_counts()

# Tạo biểu đồ pie chart
color = ("cyan","yellow","crimson")
explode = (0.1,0.1,0.1)
wp = {'linewidth':0.5, 'edgecolor':"black"}
plt.figure(figsize=(8, 8))
plt.pie(rrr, labels=rrr.index, autopct='%1.1f%%', startangle=45, shadow=True, wedgeprops=wp)
plt.axis('equal')
plt.legend(title="Note")
plt.title("Pie Chart Iris Data", loc='left', color='blue', fontsize='25')
plt.show()