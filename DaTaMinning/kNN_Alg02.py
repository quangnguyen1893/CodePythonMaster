# Make Predictions with k-nearest neighbors on the Iris Flowers Dataset
from csv import reader
from math import sqrt


# Load a CSV file
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset


# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())


# Convert string column to integer
def str_column_to_int(dataset, column):
    for row in dataset:
        row[column] = int(row[column].strip())

# Find the min and max values for each column
def dataset_minmax(dataset):
    minmax = list()
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        minmax.append([value_min, value_max])
    return minmax

# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

# Calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)):
        distance += (row1[i] - row2[i]) ** 2
    return sqrt(distance)


# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors


# Make a prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction
# read data file
fnTrain = 'data/iris/iris.trn'
fnTest = 'data/iris/iris.tst'
trainSet = load_csv(fnTrain)
testSet = load_csv(fnTest)
# Normolize Train set
for i in range(len(trainSet[0]) - 1):
    str_column_to_float(trainSet, i)
str_column_to_int(trainSet, len(trainSet[0]) - 1)
# trainS = [tple[:-1] for tple in trainSet]
# minmaxTrainset = dataset_minmax(trainS)
# normalize_dataset(trainS,minmaxTrainset)
# Normolize Test set
for i in range(len(testSet[0]) - 1):
    str_column_to_float(testSet, i)
str_column_to_int(testSet, len(testSet[0]) - 1)
labelActual = [tple[4] for tple in testSet]
# minmaxTestset = dataset_minmax(testSet)
# normalize_dataset(testSet,minmaxTestset)
testSet = [tple[:-1] for tple in testSet]
# Input k
so_k = int(input("Nhập K: "))
# predict the label
correct = 0
for i in range(len(testSet)):
    printPredic = predict_classification(trainSet, testSet[i], so_k)
    print('Data=%s, Predicted: %s' % (testSet[i], printPredic))
    if labelActual[i] == printPredic:
        correct += 1
rate = correct / float(len(testSet)) * 100.0
print('Ti le du doan: ',rate)

# dang toi phan chuan hoa du lieu - co can chuan hoa label hay khong