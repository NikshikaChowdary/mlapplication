import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'semester':['Sem 1', 'Sem 2', 'Sem 3', 'Sem 4', 'Sem 1', 'Sem 2', 'Sem 3', 'Sem 4', 'Sem 1', 'Sem 2'],
    'hours_studied': [2, 9, 10, 4, 3, 9, 11, 7, 12, 5]
}

df = pd.DataFrame(data)

plt.figure(figsize=(4,2))
sns.boxplot(x='semester', y='hours_studied', data=df)
plt.title('Student Performance: Studied by Semester')
plt.xlabel('Semester')
plt.ylabel('Number of Hours Studied')

plt.show()