import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

data = []
with open('segment.data', 'r') as file:
    for line in file:
        values = list(map(float, line.strip().split())) 
        data.append(values)

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=[f'{i}' for i in range(1, len(data[0]) + 1)])
class_labels = df[f'{len(data[0])}']
df = df.iloc[:, :-1] #lấy 20 cột

df['class'] = class_labels # gán làm tên lớp
df = df.sort_values('class')

# Plot the Parallel Coordinate plot
plt.figure(figsize=(12, 6))
parallel_coordinates(df, 'class')
plt.title('Parallel Coordinate Plot of Data Segment')
plt.show()
