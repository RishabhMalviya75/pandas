import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 25,90, 90,56],
    'salary': [2000,10003,4000,5000,7600]
}
df = pd.DataFrame(data)
group = df.groupby("Age")["salary"].sum()
print(group)