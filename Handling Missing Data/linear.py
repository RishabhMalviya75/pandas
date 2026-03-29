import pandas as pd 
Data = {
    'Time': [1,2,3,4,5  ,6,7,8,9,10],
    'Value': [10,20,None,40,50,None,70,80,None,100]
}
df = pd.DataFrame(Data)
print(df)
# Linear Interpolation
print("\nLinear Interpolation:")
df['Value'] = df['Value'].interpolate(method='linear')
print(df)