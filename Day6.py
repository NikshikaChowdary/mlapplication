import pandas as pd

# Data for the DataFrame
data = {
    "Name": ["John", "Alice", "Bob", "Diana"],
    "Age": [28, 34, 23, 29],
    "Department": ["HR", "IT", "Marketing", "Finance"],
    "Salary": [45000, 60000, 35000, 50000],
}

# Create the DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)



import pandas as pd

# Data for the DataFrame
data = {
    "Name": ["John", "Alice", "Bob", "Diana"],
    "Age": [28, 34, 23, 29],
    "Department": ["HR", "IT", "Marketing", "Finance"],
    "Salary": [45000, 60000, 35000, 50000],
}

# Create the DataFrame
df = pd.DataFrame(data)

# 1. Display the first 2 rows of the DataFrame
print("First 2 rows of the DataFrame:")
print(df.head(2))

# 2. Add a new column named `Bonus` where the bonus is 10% of the salary
df["Bonus"] = df["Salary"] * 0.10
print("\nDataFrame after adding the Bonus column:")
print(df)

# 3. Calculate the average salary of employees in the DataFrame
average_salary = df["Salary"].mean()
print(f"\nThe average salary of employees is: {average_salary}")

# 4. Filter and display employees who are older than 25
filtered_employees = df[df["Age"] > 25]
print("\nEmployees who are older than 25:")
print(filtered_employees)
