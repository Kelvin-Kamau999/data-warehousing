import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from CSV file
data = pd.read_csv('data2.csv')

# Create a pivot table with counts of each product type for each product name
pivot = pd.pivot_table(data, values='product_id', index='product_name', columns='product_type', aggfunc=len, fill_value=0)

# Create the heatmap using seaborn
heatmap = sns.heatmap(pivot, cmap='YlGnBu')

# Customize the plot
heatmap.set_title('Product Type by Product Name')
heatmap.set_xlabel('Product Type')
heatmap.set_ylabel('Product Name')

# Show the plot
plt.show()