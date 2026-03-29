import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 20, 90, 78, 56],
    'salary': [2000,10003,4000,5000,7600]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df.sort_values(by=["Age", "salary"], ascending=[True, True],  inplace=True)
print("\nSorted DataFrame:") 
print(df)       
