import pandas as pd
data={
    "marks": [99,98,100,99,],
    "SubjectName": ["Social","Science","Maths","English"],
    "grade": ["A+","A+","O","A+"]

}
df=pd.DataFrame(data)
print(df)