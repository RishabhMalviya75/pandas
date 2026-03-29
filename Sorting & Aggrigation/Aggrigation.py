import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 20, 90, 78, 56],
    'salary': [2000,10003,4000,5000,7600]
}
df = pd.DataFrame(data)
avg_salary = df['salary'].mean()
print("Average Salary:", avg_salary)
total_salary = df['salary'].sum()
print("Total Salary:", total_salary)
max_salary = df['salary'].max()
print("Maximum Salary:", max_salary)
min_salary = df['salary'].min()
print("Minimum Salary:", min_salary)
median_salary = df['salary'].median()
print("Median Salary:", median_salary)
std_salary = df['salary'].std()
print("Standard Deviation of Salary:", std_salary)
var_salary = df['salary'].var()
print("Variance of Salary:", var_salary)
count_salary = df['salary'].count()
print("Count of Salary:", count_salary)
mode_salary = df['salary'].mode()
print("Mode of Salary:", mode_salary)
