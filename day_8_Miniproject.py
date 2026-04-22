import pandas as pd
df = pd.read_csv('students.csv', skipinitialspace=True)
df.columns = df.columns.str.strip()
#print(df)
#print(df.isnull())
#cleaning data
df.fillna(df.mean(numeric_only=True), inplace=True)
#average
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)
#grouping
df['result'] = df['Average'].apply(lambda x: "pass" if x>=75 else 'Fail')
#filter toppers
toppers = df[df['Average'] > 80]
failed = df[df['Average'] <= 75]
pased = df[df['Average'] >= 75]
passed_count = pased.shape[0]
print('all data :\n',df)
print('toppers :\n',toppers)
print('failed :\n',failed)
print('Number of passed Students :',passed_count)
print(df.groupby('result').count())
















