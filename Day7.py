# Importing pandas
import pandas as pd

# Loading the dataset
file_path = "sales_data.csv"  # Replace with the actual file path
sales_data = pd.read_csv(file_path)

# Displaying the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(sales_data.head())

# Displaying basic statistics of the numerical columns
print("\nBasic statistics of numerical columns:")
print(sales_data.describe())
