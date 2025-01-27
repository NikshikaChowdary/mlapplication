import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set seed for reproducibility
np.random.seed(10)

# Generate data
data = pd.DataFrame({
    'value': np.concatenate([np.random.normal(0, 1, 100), np.random.normal(10, 1, 10)])
})

# Calculate quartiles and IQR
Q1 = data['value'].quantile(0.25)
Q3 = data['value'].quantile(0.75)
IQR = Q3 - Q1

# Calculate bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers = data[(data['value'] < lower_bound) | (data['value'] > upper_bound)]

print(f"Outliers based on box plot:\n{outliers}")

# Plotting
plt.figure(figsize=(12, 6))

# Box plot
plt.subplot(1, 2, 1)
sns.boxplot(x=data['value'])
plt.title('Box Plot')

# Violin plot
plt.subplot(1, 2, 2)
sns.violinplot(x=data['value'])
plt.title('Violin Plot')

plt.tight_layout()
plt.show()

