import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 25 ,90, 78, 78],
    'salary': [2000,10003,2000,5000,2000]
}
df = pd.DataFrame(data)
group = df.groupby(['Age','Name'])['salary'].sum()
print(group)