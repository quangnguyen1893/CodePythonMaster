import numpy as np

class kNN:
    def __init__(self, k=3):
        self.k = k

    def set_datatrain(self, X, y):
        self.X_train = X
        self.y_train = y

    def dudoan_labels(self, X):
        nhan_dubao = []
        for x in X:
            # Tính khoảng cách giữa điểm dữ liệu mới và các điểm dữ liệu huấn luyện
            distances = [khoangcach(x, x_train) for x_train in self.X_train]
            cacdiemgan = np.argsort(distances)[:self.k] #sắp lại và láy điểm gần nhất
            diemgannhat = [self.y_train[i] for i in cacdiemgan]
            nhan_diemgannhat = max(set(diemgannhat), key=diemgannhat.count)
            nhan_dubao.append(nhan_diemgannhat)
        return np.array(nhan_dubao)

# tính khoảng cách giữa hai điểm dữ liệu
def khoangcach(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

file_train = input("Nhập file train: ")
file_test = input("Nhập file test: ")
so_k = int(input("Nhập k: "))

#tập dữ liệu train
data_list_train = []
with open(file_train) as file:
    for line in file:
        value = line.strip().split(",")
        data = [float(x) for x in value]
        data_list_train.append(data)

data_train_array = np.array(data_list_train)
data_train_X = data_train_array[:, :-1] # lấy các cột trước làm feature
label_train_y = data_train_array[:, -1] # lấy cột cuối cùng làm nhãn

#tập dữ liệu test
data_list_test = []
with open(file_test) as file:
    for line in file:
        value = line.strip().split(",")
        data = [float(x) for x in value]
        data_list_test.append(data)

data_test_array = np.array(data_list_test)
data_test_X = data_test_array[:, :-1] # lấy các cột trước làm feature
label_test_y = data_test_array[:, -1] # lấy cột cuối cùng làm nhãn

knn = kNN(k=so_k) #thay đổi k theo đề bài
knn.set_datatrain(data_train_X, label_train_y)

#dự đoán nhãn cho dữi liệu mới
new_y = knn.dudoan_labels(data_test_X)

labels_dung = np.sum(new_y == label_test_y)
tongsotest = len(label_test_y)
dochinhxac = labels_dung / tongsotest
print("Độ chính xác: %.2f%%" % (dochinhxac * 100))
print(new_y)