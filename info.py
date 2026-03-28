import pandas as pd 
df = pd.read_json("output.json", orient='records')
print("display the information of dataframe")

print(df.info())