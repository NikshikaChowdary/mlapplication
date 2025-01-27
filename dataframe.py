import pandas as pd
data=[20,13,34,22,19,45,86,96,72,48,65,28,91,4]
No_of_studied=data[4:8]
print("hours studied",No_of_studied)
Age=data[9:13]
print("Student_age",Age)
screen_time=data[5:14]
Data_Frame=pd.DataFrame(data)
print(Data_Frame)