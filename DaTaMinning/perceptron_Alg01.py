import pandas as pd
import numpy as np


def perceptron_train(train_data, eta, max_iter):
    train_data = train_data.values
    n = train_data.shape[1] - 1
    w = np.zeros(n)
    b = 0
    converged = False
    iter = 0
    while not converged and iter < max_iter:
        converged = True
        for i in range(train_data.shape[0]):
            x = train_data[i, :n]
            y = train_data[i, n]
            if y * (np.dot(w, x) + b) <= 0:
                w = w + eta * y * x
                b = b + eta * y
                converged = False
        iter += 1
    return w, b


def perceptron_predict(test_data, w, b):
    test_data = test_data.values
    n = test_data.shape[1] - 1
    y_true = test_data[:, n]
    y_pred = np.zeros(y_true.shape)
    for i in range(test_data.shape[0]):
        x = test_data[i, :n]
        y = np.sign(np.dot(w, x) + b)
        y_pred[i] = y
    return y_true, y_pred


def accuracy(y_true, y_pred):
    acc = (y_true == y_pred).mean()
    acc_pos = ((y_true == 1) & (y_pred == 1)).sum() / (y_true == 1).sum()
    acc_neg = ((y_true == -1) & (y_pred == -1)).sum() / (y_true == -1).sum()
    return acc, acc_pos, acc_neg


if __name__ == '__main__':
    # Đọc tập dữ liệu từ file Spam (hold-out)
    data = pd.read_csv('data/spam/spam.data', header=None)
    # Phân chia dataframe thành hai phần: 80% dữ liệu làm tập huấn luyện và 20% dữ liệu làm tập kiểm thử
    train_data = data.sample(frac=0.8, random_state=1)
    test_data = data.drop(train_data.index)
    eta = 0.3
    max_iter = 50
    w, b = perceptron_train(train_data, eta, max_iter)
    y_true, y_pred = perceptron_predict(test_data, w, b)
    acc, acc_pos, acc_neg = accuracy(y_true, y_pred)
    print('Độ chinh xác:', acc)
    print('Độ chính xác trên lớp 1:', acc_pos)
    print('Độ chính xác trên lớp -1:', acc_neg)
    print('Bảng tổng kết:')
    print(pd.crosstab(y_true, y_pred, rownames=['True'], colnames=['Dự đoán'], margins=True))
