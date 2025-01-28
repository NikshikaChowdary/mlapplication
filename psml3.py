import pandas as pd
import numpy as np
def createdata():
  data={
    'Brand': ['Maruti', 'Hyundai', 'Tata', 'Mahindra', 'Maruti', 'Hyundai', 'Renault', 'Maruti', 'Tata'],
    'Year': [2012, 2014, 2011, 2015, 2012, 2016, 2014, 2018, 2019],
    'KMS Driven': [50000, 30000, 60000, 25000, 10000, 46000, 31000, 15000, 12000],
    'City': ['Gurgaon', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Chennai', 'Ghaziabad','Pune','Zaheerabad'],
    'Mileage': [28, 27, 25, 26, 28, 29, 24, 21, 24]
 }
  df=pd.DataFrame(data)
  return df
df=createdata()
df.head(10)