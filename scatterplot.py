import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Correcting the data to ensure all lists have equal lengths
data = {
    'Temperature': [22, 33, 45, 67, 32, 44, 67, 89, 32, 54, 50, 60, 35, 44, 67, 87, 23, 76, 78, 98, 35, 46],
    'Humidity': [56, 45, 87, 45, 68, 54, 27, 58, 81, 32, 43, 78, 76, 54, 27, 98, 13, 18, 81, 79, 64, 72],
    'Wind Speed': [12, 10, 15, 32, 22, 18, 20, 25, 30, 28, 14, 16, 18, 22, 20, 25, 10, 15, 32, 14, 18, 20],
    'Pressure': [1025, 1012, 1017, 1014, 1013, 1016, 1018, 1015, 1019, 1020, 1021, 1011, 1013, 1015, 1017, 1018, 1014, 1012, 1020, 1022, 1023, 1016],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Temperature'], df['Humidity'], color='red', label='Temp vs Humidity')

# Adding labels and title
plt.title('Temperature vs Humidity', fontsize=14)
plt.xlabel('Temperature (°C)', fontsize=12)
plt.ylabel('Humidity (%)', fontsize=12)
plt.legend()

# Display the plot
plt.show()
