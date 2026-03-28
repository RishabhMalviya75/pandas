import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']

}
df =pd.DataFrame(data)
print(df)
# save the dataframe to a JSON file
df.to_json('output.json', orient='records')