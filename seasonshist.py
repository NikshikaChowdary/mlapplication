import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
datf=pd.DataFrame({"Season 1":[7,4,5,6,3],
                   "season 2":[1,4,5,3,7]})
p=sns.histplot(data=datf)
p.set(xlabel="X label value",ylabel="Y label value")
plt.show()
