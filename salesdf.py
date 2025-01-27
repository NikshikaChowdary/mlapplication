import pandas as pd
sales_data={
    'TransactionID':['1','2','3','4'],
    'CustomerID':['101','102','103','104'],
    'Amount':[250,350,450,550],
}
customer_data={
    'CustomerID':[101,102,103,104],
    'CustomerName':['Aice','Bob','cap','dag'],
    'Age':[20,30,40,50],
    'city':['LA','NY','SA','BZ']
    }
sales_df=pd.DataFrame(sales_data)
customer_df=pd.DataFrame(customer_data)
print(sales_df)
print(customer_df)


