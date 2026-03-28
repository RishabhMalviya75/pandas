import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi'],
    'Age': [25, 30, 35, 40, 45, 50, 55, 60 ],
    'Salary': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000],
    'performance-score': [85, 80, 75, 70, 65, 60, 55, 50]
}

df = pd.DataFrame(data)
print(df)
print("selecting  a single columns return series")
print(df['Name'])
print("multiple columns return dataframe")
print(df[['Name', 'Age']])