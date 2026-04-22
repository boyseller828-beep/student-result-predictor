import pandas as pd
df = pd.read_csv('students.csv')
#avarage marks
df['Average'] = df[['Math','Science','English']].mean(axis=1)
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 75 else "Fail")
print(df)
#topper
topper = df.loc[df['Average'].idxmax()]
print("topper is :\n")
print(topper)
print(df.sort_values(by="Average", ascending=False))


















