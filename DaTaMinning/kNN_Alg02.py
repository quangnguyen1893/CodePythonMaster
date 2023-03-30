from math import sqrt
import numpy as np

# Step 1: Tinh khoang cach Euclid
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)):
        distance += (row1[i] - row2[i]) ** 2
    return sqrt(distance)

# Step 2: Chon nhung hang xom gan theo tieu chi
def get_neighbors(trainSet, target, num_neighbors):
    distances = list()
    for train_row in trainSet:
        dist = euclidean_distance(target, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors

# Step 3: Du doan
def predict_func(trainSet, target, num_neighbors):
    neighbors = get_neighbors(trainSet, target, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction

dataset = [[0.376000, 0.488000, 0],
           [0.312000, 0.544000, 0],
           [0.298000, 0.624000, 0],
           [0.394000, 0.600000, 0],
           [0.506000, 0.512000, 0],
           [0.488000, 0.334000, 1],
           [0.478000, 0.398000, 1],
           [0.606000, 0.366000, 1],
           [0.428000, 0.294000, 1],
           [0.542000, 0.252000, 1]]

# print(dataset)
gessSet = [[0.550000, 0.364000],
           [0.558000, 0.470000],
           [0.456000, 0.450000],
           [0.450000, 0.570000]]

so_k = int(input("Nhập K: "))
for predic in gessSet:
    printPredic = predict_func(dataset, predic, so_k)
    print('Du doan cho phan tu',predic,'thuoc lop',printPredic, '\n')

