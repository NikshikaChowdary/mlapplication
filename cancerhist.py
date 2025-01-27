import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)
data = np.random.randint(20, 81, 1000)
plt.hist(data,bins=15,edgecolor='black',color='skyblue')
plt.title('hist of cancer patient age distribution')
plt.xlabel('age')
plt.ylabel('number of patients')

plt.show()
