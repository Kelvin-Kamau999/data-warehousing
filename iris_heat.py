import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset from seaborn
iris = sns.load_dataset('iris')

# Create a pivot table that counts the occurrences of each species
pivot_table = iris.pivot_table(index='species', values='sepal_length', aggfunc='count')

# Plot the pivot table as a heatmap
sns.heatmap(pivot_table, cmap='YlGnBu', annot=True, fmt='d')
plt.title('Species Count')
plt.xlabel('Sepal Length')
plt.ylabel('Species')

# Display the heatmap
plt.show()
