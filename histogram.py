import matplotlib.pyplot as plt
data=[5,7,7,8,9,10,10,11,12,11,11]
plt.hist(data,bins=10,edgecolor='black')
plt.title('simple histogram ex')
plt.xlabel('numbers')
plt.ylabel('count')
plt.show()
