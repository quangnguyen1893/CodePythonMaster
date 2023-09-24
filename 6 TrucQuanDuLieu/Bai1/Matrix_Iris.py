import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data from the text file
file_path = "D:/Master/Master-Code/CodePythonMaster/6 TrucQuanDuLieu/Bai1/data/iris.data"
data = []
with open(file_path, 'r') as file:
    for line in file:
        values = line.strip().split(',')
        data.append(values)

# Create a DataFrame
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df = pd.DataFrame(data, columns=column_names)

# Convert numeric columns to numeric types, handling empty strings
numeric_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Remove rows with missing values
df.dropna(inplace=True)

# Create a pairplot using Seaborn
sns.pairplot(df, hue='species', markers=["o", "s", "D"])

# Show the plot
plt.show()
