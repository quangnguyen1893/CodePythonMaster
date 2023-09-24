import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

data = pd.read_csv('iris.data', header=None)

# Xác định tên cột và dữ liệu
column_names = data.columns.tolist()
class_column = column_names[-1]  # cột cuối là class
feature_columns = column_names[:-1]  #

# Vẽ biểu đồ Parallel Coordinate
plt.figure(figsize=(10, 6))
parallel_coordinates(data, class_column, color=['r', 'g', 'b'])
plt.title('Parallel Coordinate Plot of Data Iris')
plt.show()
