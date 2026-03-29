import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 20, 90, 78, 56]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df.sort_values(by="Age", ascending=False, inplace=True)
print("\nSorted DataFrame:")
print(df)