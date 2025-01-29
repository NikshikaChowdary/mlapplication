# Importing pandas
import pandas as pd

# Loading the dataset
file_path = "sales_data.csv"  # Replace with the actual file path
sales_data = pd.read_csv(file_path)

# Extracting all rows where sales are greater than 1000
print("Rows where sales are greater than 1000:")
sales_greater_than_1000 = sales_data[sales_data["Sales"] > 1000]
print(sales_greater_than_1000)

# Finding all sales records for a specific region (e.g., "East")
region = "East"  # Replace with the desired region name
print(f"\nSales records for the region '{region}':")
sales_in_region = sales_data[sales_data["Region"] == region]
print(sales_in_region)
