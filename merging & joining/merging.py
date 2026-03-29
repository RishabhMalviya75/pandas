import pandas as pd 
df_customers = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45]
})
df_orders = pd.DataFrame({
    'OrderID': [101, 102, 103, 104, 105],
    'CustomerID': [1, 2, 2, 3, 5],
    'Amount': [250, 150, 200, 300, 400]
})
merged_df = pd.merge(df_customers, df_orders, on='CustomerID', how='inner')
print(merged_df)
merged_df = pd.merge(df_customers, df_orders, on='CustomerID', how='outer')
print(merged_df)
merged_df = pd.merge(df_customers, df_orders, on='CustomerID', how='left')
print(merged_df)
merged_df = pd.merge(df_customers, df_orders, on='CustomerID', how='right')
print(merged_df)