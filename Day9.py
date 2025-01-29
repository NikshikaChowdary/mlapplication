import pandas as p
patient_data = {'Patient Name': ['Ram', 'Shyam', 'Asad', 'Karthik'],'Age': [5, 7, 3, 10],'Date of appointment': ['2025-01-20', '2025-01-21', '2025-01-22', '2025-01-23'], 'Patient id': [101, 102, 103, 104]}
drag_data = {'Drag Name': ['Medicine A', 'Medicine B', 'Medicine C', 'Medicine D'],'Quantity': [2, 3, 1, 5],'Patient id': [101, 102, 103, 104]}
df_patient = p.DataFrame(patient_data)
df_drag = p.DataFrame(drag_data)
df_patient_filtered = df_patient[df_patient['Age'] < 6]
df_merged = p.merge(df_patient_filtered, df_drag, on='Patient id', how='inner')
df_merged
     
Patient Name	Age	Date of appointment	Patient id	Drag Name	Quantity
0	Ram	5	2025-01-20	101	Medicine A	2
1	Asad	3	2025-01-22	103	Medicine C	1