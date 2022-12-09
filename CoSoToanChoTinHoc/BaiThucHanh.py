
# https://drive.google.com/drive/folders/1BZSFCIu-9THdggcPwN-uaLpvKES1Zrvr
# Bài tập 1:
# Lắp ráp các đoạn chương trình trên thành chương trình hoàn chỉnh làm các công việc sau:
# - Đọc dữ liệu từ file ex1data1.txt, chuyển thành mảng lưu vào data
# - Tính số hàng và số cột lưu vào m, n
# - Tách n-1 cột đầu tiên lưu vào X, cột cuối lưu vào y
# - Thêm 1 cột chứa toàn số 1 vào cột 0 của X
# - Áp dụng 1 trong phương pháp chính xác tìm theta lưu vào theta1
# - Áp dụng phương pháp gradient descent để tìm theta với giá trị khởi tạo = 0, bước nhảy
# alpha = 0.01 và số bước lặp = 2000, lưu kết quả vào theta2
# - In theta1 và theta2 ra màn hình để so sánh
# - Vẽ dữ liệu và đường thẳng hồi quy lên cùng một đồ thị

# import numpy as np
# import matplotlib.pyplot as plt
# text_file = open("ex1data1.txt", "r")
# lines = text_file.readlines()
# data = np.array([[float(x) for x in line.split(",")] for line in lines])
# m,n = data.shape
# # *** tính theta bằng phương pháp chính xác
# X = data[:, range(n-1)]
# Y = data[:,-1]
# X = np.insert(X,0,1,axis=1)
# A = np.dot(X.T, X)
# theta1 = np.dot(np.dot(np.linalg.inv(A), X.T), Y)
# print("theta1= ", theta1)
# # *** tính theta theo gradient descent
# theta2 = np.zeros(n)
# alpha = 0.01
# nb_it = 2000
# for it in range(nb_it):
#     gradient = (np.dot((np.dot(X.T, X)),theta2) - (np.dot(X.T, Y)))/m
#     theta2 = theta2 - alpha*gradient
# print("theta2= ", theta2)
# h1 = np.dot(X, theta1)
# h2 = np.dot(X, theta2)
# plt.plot(data[:,0], data[:,-1], 'ro')
# plt.xlabel('Area')
# plt.ylabel('Price')
# plt.plot(data[:,0], h1)
# plt.plot(data[:,0], h2)
# plt.show()
# ===============================================================================================================
# Bài tập 2:
# Làm tương tự bài tập 1 nhưng trên tập dữ liệu ex1data2.txt. Bài tập này ta không cần vẽ đồ
# thị.
# Chú ý:
# - Tập dữ liệu này có 3 cột: 2 cột đầu là X, cột cuối là y.
# - Kết quả của phương pháp gradient descent không giống với phương pháp chính xác vì
# 2 cột có giá trị quá khác nhau (thực ra là cả 3 cột khác nhau nếu tính luôn cột 0 có giá
# trị bằng 1).
# - Để có kết quả tương tự nhau ta cần chuẩn hoá dữ liệu.

# import numpy as np
# text_file = open("ex1data2.txt", "r")
# lines = text_file.readlines()
# data = np.array([[float(x) for x in line.split(",")] for line in lines])
# m,n = data.shape
# X = data[:, range(n-1)]
# Y = data[:,-1]
# X = np.insert(X,0,1,axis=1)
# A = np.dot(X.T, X)
# # *** tính theta bằng phương pháp chính xác
# theta1 = np.dot(np.dot(np.linalg.inv(A), X.T), Y)
# print("theta1= ", theta1)
# # # *** tính theta theo gradient descent
# theta2 = np.zeros(n)
# alpha = 0.0000001
# nb_it = 2000
# for it in range(nb_it):
#     gradient = (np.dot((np.dot(X.T, X)),theta2) - (np.dot(X.T, Y)))/m
#     theta2 = theta2 - alpha*gradient
# print("theta2= ", theta2)
# ===============================================================================================================
# Bài tập 3: Chuẩn hoá dữ liệu
# Ta cần chuẩn hoá các cột dữ liệu của X sao cho có mean = 0 và độ lệch chuẩn = 1.
# Với mỗi cột j,
# Tính giá trị trung bình mean và độ lệch chuẩn sigma (numpy.mean(), numpy.std()).
# Chuẩn hoá theo công thức:
# X[:, j] = (X[:, j] – mean)/sigma
# Sau đó chạy phần tìm theta bằng phương pháp gradient.
# So sánh kết quả thu được với phương pháp chính xác.

import numpy as np
text_file = open("ex1data2.txt", "r")
lines = text_file.readlines()
data = np.array([[float(x) for x in line.split(",")] for line in lines])
#số hàng và số cột lưu vào m, n
m,n = data.shape
X = data[:, range(n-1)]
Y = data[:,-1]
# chuẩn hóa dữ liệu X
#mỗi cột j, cột ở vị trí 1
c=0
while(c==0):
    for j in range(1,X.shape[1]):
        sigma = np.std(X[:, j])
        mean = np.mean(X[:, j])
        X[:, j] = (X[:, j] + (-mean)) / sigma
        if round(mean,2)==0 and round(sigma,2)==1.0:
            c=1
            break
X = np.insert(X,0,1,axis=1)
theta = np.zeros(n)
alpha = 0.0000001
nb_it = 2000
for it in range(nb_it):
    gradient = (np.dot((np.dot(X.T, X)),theta) - (np.dot(X.T, Y)))/m
    theta = theta - alpha*gradient
print("theta2= ", theta)

# ===============================================================================================================
# 4. Phân tích thành phần chính
# Cho tập dữ liệu X có m hàng n cột. Phân tích thành phần chính (PCA) tìm k thành phần chính
# của tập dữ liệu này (k << n). k thành phần chính chứa hầu hết các thông tin của X. Dùng k
# thành phần chính có thể phục hồi lại X gần giống như ban đầu.
# Các bước thực hiện
# a. Tìm thành phần chính
# b. Giảm chiều của X (chiếu X lên không gian thành phần chính)
# c. Phục hồi X
# ===============================================================================================================
# Bài tập 4. PCA
# - Đọc tập dữ liệu “X.csv” lưu vào biến X. Tập dữ liệu này chỉ có 2 cột (n = 2).
# - Vẽ tập dữ liệu X dùng X[:,0] là trục ngang, X[:1] là trục dọc
# plt.plot(X[:,0], X[:,1], 'ro')
# - Tìm 1 thành phần chính của X (k = 1), lưu vào Ureduce.
# - Chiếu dữ liệu gốc lên thành phần chính này, lưu kết quả vào Z.
# - Phục hồi lại X bằng cách sử dụng Z và Ureduce, lưu kết quả vào Xrestore.
# - Tính sự khác biệt trung bình giữa X và Xrestore theo công thức:









