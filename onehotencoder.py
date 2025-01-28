import pandas as pd
from sklearn.preprocessing import OneHotEncoder
data={
    "customer_id":[1,2,3,4],
    "gender":["Male","Female","Female","Male"],
    "city":["Hyderabad","pune","Bangalore","mumbai"],
    "fruits":["Apple","orange","kiwi","Banana"]
}
df=pd.DataFrame(data)
print("original dataframe")
print(df)
one_hot_encoder=OneHotEncoder(sparse_output=False)
columns_to_encode=["gender","city","fruits"]
encoded_data=one_hot_encoder.fit_transform(df[columns_to_encode])
encoded_columns=one_hot_encoder.get_feature_names_out(columns_to_encode)
encoded_df=pd.DataFrame(encoded_data,columns=encoded_columns)
print(encoded_df)
print("\none-Hot Encoded Dataframe with sklearn:")

