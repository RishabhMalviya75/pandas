import pandas as pd 
# read file from csv file into dataframe
# df  = pd.read_csv("D:\pandas\krishna_soni.csv", encoding='latin-1')
df = pd.read_json("output.json", orient='records')
print(df)