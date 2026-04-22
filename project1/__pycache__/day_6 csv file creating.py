#csv file creating
import pandas as pd

df = pd.read_csv('students.csv')
print(df)
print(df.head())
print(df.columns)
print(df['Math'])
print(df.tail(5))












