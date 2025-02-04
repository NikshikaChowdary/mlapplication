#add scatter plots for the above code
import matplotlib.pyplot as plt
plt.scatter(df['WT'],df['MPG'])
plt.scatter(df['VOL'],df['MPG'])
plt.scatter(df['SP'],df['MPG'])
plt.scatter(df['HP'],df['MPG'])