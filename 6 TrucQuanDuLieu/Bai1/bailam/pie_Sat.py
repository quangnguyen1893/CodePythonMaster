import pandas as pd
import matplotlib.pyplot as plt

data = []
with open('sat.trn', 'r') as file:
    for line in file:
        line = line.strip()
        values = line.split()
        data.append(values)

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)
# Sử dụng cột cuối cùng làm nhãn
labels = df.iloc[:, -1]
# Đếm số lượng mỗi nhãn
count_lable = labels.value_counts()
color = ("cyan","yellow","crimson")
explode = (0.1,0.1,0.1,0.1,0.1,0.1)
wp = {'linewidth':0.5, 'edgecolor':"black"}
plt.figure(figsize=(8, 8))
plt.pie(count_lable, labels=sorted(count_lable.index), autopct='%1.1f%%', startangle=45, shadow=True, wedgeprops=wp, explode=explode)
plt.axis('equal')
plt.legend(title="Note")
plt.title("Pie Chart Satellite Image Data", loc='left', color='blue', fontsize='25')
plt.show()
