import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the data from the text file
data = []
file_path = "D:/Master/Master-Code/CodePythonMaster/6 TrucQuanDuLieu/Bai1/data/iris.data"
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

# Filter the DataFrame by species
species_to_plot = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
filtered_df = df[df['species'].isin(species_to_plot)]

# Normalize the numeric columns
normalized_df = (filtered_df[numeric_columns] - filtered_df[numeric_columns].min()) / (filtered_df[numeric_columns].max() - filtered_df[numeric_columns].min())

# Concatenate normalized data and species column
normalized_df['species'] = filtered_df['species']

# Plot Starglyph
feature_names = numeric_columns
species_colors = {'Iris-setosa': 'red', 'Iris-versicolor': 'green', 'Iris-virginica': 'blue'}

plt.figure(figsize=(10, 6))
for species, color in species_colors.items():
    species_data = normalized_df[normalized_df['species'] == species]
    angles = np.linspace(0, 2 * np.pi, len(feature_names), endpoint=False)
    values = species_data[feature_names].values[0]
    values = np.concatenate((values, [values[0]]))
    angles = np.concatenate((angles, [angles[0]]))
    plt.polar(angles, values, marker='o', color=color, label=species)
    plt.fill(angles, values, alpha=0.25, color=color)

plt.xticks(angles[:-1], feature_names)
plt.title('Starglyph Plot of Iris Data')
plt.legend()

plt.show()
