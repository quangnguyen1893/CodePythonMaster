import matplotlib.pyplot as plt
import csv
from collections import defaultdict

# Đọc dữ liệu từ file CSV
data = defaultdict(list)
with open('iris.data', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if len(row) == 5:
            giatri1, giatri2, giatri3, giatri4, iris_class = row
            data[iris_class].append((float(giatri3), float(giatri4)))
#chọn giá trị 3,4 cho tập iris

class_colors = {
    'Iris-setosa': 'r',
    'Iris-versicolor': 'g',
    'Iris-virginica': 'b'
}

plt.figure(figsize=(10, 6))
for iris_class, values in data.items():
    sepal_length = [x[0] for x in values]
    sepal_width = [x[1] for x in values]
    plt.scatter(sepal_length, sepal_width, label=iris_class,  color=class_colors[iris_class])

plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('2D Scatter Plot of Iris Classes')
plt.legend()
plt.show()
