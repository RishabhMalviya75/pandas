import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi'],
    'Age': [25, 30, 35, 40, 45, 50, 55, 60 ],
    'Salary': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000],
    'performance-score': [85, 80, 75, 70, 65, 60, 55, 50]
}

df = pd.DataFrame(data)
print(df)
higher_salary = df[df['Salary'] > 80000]
print(f"Employees with salary greater than 80000:\n{higher_salary}")

#multiple conditions
higher_salary_performance = df[(df['Salary'] > 80000) & (df['performance-score'] > 60)]
print(f"Employees with salary greater than 80000 and performance score greater than 60:\n{higher_salary_performance}")
higher_salary_performance = df[(df['Salary'] > 80000) | (df['performance-score'] > 60)]