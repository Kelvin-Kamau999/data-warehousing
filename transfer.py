import pandas as pd

# Load the data from the CSV file
df = pd.read_csv("OnlineRetail.csv")

# Create a new dataframe with the first 300 entries
df_new = df.head(1000)

# Export the new dataframe to a CSV file
df_new.to_csv("OnlineRetail_300.csv", index=False)