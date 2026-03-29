import pandas as pd
data = {
    'Name': ['Alice', None, 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi'],
    'Age': [25, None,35, 40, 45, 50, 55, 60 ],
    'Salary': [50000, None, 70000, 80000, 90000, 100000, 110000, 120000],
    'performance-score': [85, None, 75, 70, 65, 60, 55, 50]
}

df = pd.DataFrame(data)
print(df)
print("after filling missing values with 0:")
# Replace missing names with a string, and missing numbers with 0
# df.fillna({
#     'Name': 'Unknown',
#     'Age': 0,
#     'Salary': 0,
#     'performance-score': 0
# }, inplace=True)
# print(df)  

df['Age'] = df['Age'].fillna(df['Age'].mean(), inplace=True)
print(df)