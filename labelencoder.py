import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Sample data
data = {
    'Ranks': ['First', 'Second', 'First', 'Third', 'Second'],
    'fruits': ['Apple', 'Banana', 'Apple', 'Orange', 'Banana']
}

df = pd.DataFrame(data)
print("Original dataframe:")
print(df)

# Create a LabelEncoder object
label_encoder = LabelEncoder()

# Apply label encoding to 'Ranks' and 'fruits' columns
df['ranks'] = label_encoder.fit_transform(df['Ranks'])
df['fruits'] = label_encoder.fit_transform(df['fruits'])

print("\nDataFrame after label encoding:")
print(df)
