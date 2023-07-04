import csv
import numpy as np
import matplotlib.pyplot as plt
# rows = []
# with open("X.csv", "r") as file:
#     csvreader = csv.reader(file)
#     header = next(csvreader)
#     for row in csvreader:
#         rows.append(row)
# print(header)
# print(rows)


text_file = open("CoSoToanChoTinHoc/ex1data1.txt", "r")
lines = text_file.readlines() #Đọc tất cả các hàng
#chuyển toàn bộ nội dung file thành numpy.array
data = np.array([[float(x) for x in line.split(",")] for line in lines])
m, n = data.shape #m: hàng, n: cột

plt.plot(data[:,0], data[:,1], 'ro') #r: màu đỏ, o: chấm tròn
plt.xlabel('Area') #đặt nhãn cho trục x (ngang) là Area
plt.ylabel('Price') #đặt nhãn cho trục y (dọc) là Price
plt.show()