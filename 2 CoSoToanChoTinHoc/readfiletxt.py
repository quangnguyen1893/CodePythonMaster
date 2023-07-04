import numpy as np
import matplotlib.pyplot as plt
# mở file
text_file = open("ex1data1.txt", "r")
# đọc file
lines = text_file.readlines()
#chuyển toàn bộ nội dung file thành numpy.array
data = np.array([[float(x) for x in line.split(",")] for line in lines])
m, n = data.shape #m: hàng, n: cột

# ve do thi
plt.plot(data[:,0], data[:,1], 'ro') #r: màu đỏ, o: chấm tròn
plt.xlabel('Area') #đặt nhãn cho trục x (ngang) là Area
plt.ylabel('Price') #đặt nhãn cho trục y (dọc) là Price
# plt.show()
# hoi quy tuyen tinh
    # theo pp chinh xac
X = data[:, range(n-1)] # lấy n-1 cột đầu tiên của data
Y = data[:, -1] #lấy cột cuối của data (-1: cột cuối)
#thêm cột 0 có giá trị = 1 vào X, (axis=1: thêm cột, axis=0: thêm hàng)
X = np.insert(X, 0, 1, axis=1)
A = np.dot(X.T, X)
# theta = np.dot(np.dot(np.linalg.inv(A), X.T), y)
# hoac
# theta, _, _, _ = np.linalg.lstsq(X, y)
    # theo pp giam gradien
#Khởi tạo theta = 0, theta có n phần tử
theta = np.zeros(n)
alpha = 0.01 #bước nhảy
nb_it = 1500 #số lần lặp
# theta2
theta2 = np.zeros(n)
alpha2 = 0.01 #bước nhảy
nb_it2 = 2000 #số lần lặp
for it in range(nb_it):
    gradient = (np.dot((np.dot(X.T, X)), theta) - (np.dot(X.T, Y))) / m
    theta = theta - alpha * gradient
for it in range(nb_it2):
    gradient2 = (np.dot((np.dot(X.T, X)), theta2) - (np.dot(X.T, Y))) / m
    theta2 = theta2 - alpha * gradient2
print(theta , '', theta2)
#ve duong thang
    #Tính giá trị dự báo với theta tìm được
h = np.dot(X, theta)
h2 = np.dot(X, theta2)
    #Vẽ lại dữ liệu gốc
plt.plot(data[:,0], data[:,-1], 'ro')
plt.xlabel('Area')
plt.ylabel('Price')
    #Vẽ giá trị dự báo chồng lên
plt.plot(data[:,0], h)
plt.plot(data[:,0], h2)
plt.show()