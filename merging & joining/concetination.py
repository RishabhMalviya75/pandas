import pandas as pd 
df_region1 = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
})
df_region2 = pd.DataFrame({
    'CustomerID': [4, 5, 6],
    'Name': ['David', 'Eve', 'Frank'],
})
df_concatenated = pd.concat([df_region1, df_region2], ignore_index=True , axis=1)   #axis=1 means we are concatenating along the columns, so the resulting DataFrame will have the columns from both df_region1 and df_region2. If we had used axis=0, it would concatenate along the rows, stacking the DataFrames on top of each other.
print(df_concatenated)                                                             #axis=0 means we are concatenating along the rows, so the resulting DataFrame will have the rows from both df_region1 and df_region2 stacked on top of each other. If we had used axis=1, it would concatenate along the columns, combining the DataFrames side by side.