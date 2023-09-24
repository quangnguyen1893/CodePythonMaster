import matplotlib.pyplot as plt
import csv
from collections import defaultdict

# Đọc dữ liệu từ file CSV
list_values = []
data = defaultdict(list)
with open('sat.trn', 'r') as file:
    for line in file:
        values = list(map(float, line.strip().split())) 
        list_values.append(values)
    for row in list_values:
        if len(row) == 37:
            giatri1, giatri2, giatri3, giatri4, giatri5, giatri6, giatri7, giatri8, giatri9, giatri10, giatri11, giatri12, giatri13, giatri14, giatri15, giatri16, giatri17, giatri18, giatri19, giatri20, giatri21, giatri22, giatri23, giatri24, giatri25, giatri26, giatri27, giatri28, giatri29, giatri30, giatri31, giatri32, giatri33, giatri34, giatri35, giatri36, sat_class = row
            data[int(sat_class)].append((float(giatri2), float(giatri36)))
#chọn giá trị 

class_colors = {
    1: 'r',
    2: 'g',
    3: 'b',
    4: 'c',
    5: 'm',
    6: 'y',
    7: 'k'
}

sorted_data = {k: data[k] for k in sorted(data.keys())}

plt.figure(figsize=(10, 6))
for sat_class, values in sorted_data.items():
    VALUE1 = [x[0] for x in values]
    VALUE2 = [x[1] for x in values]
    plt.scatter(VALUE1, VALUE2, label=sat_class,  color=class_colors[sat_class])

plt.xlabel('Giá trị 1')
plt.ylabel('Giá trị 2')
plt.title('2D Scatter Plot of Iris Classes')
plt.legend()
plt.show()
