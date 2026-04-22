import pandas as pd

df = pd.read_csv('my_Family.csv')
#df.loc[2, 'B'] = None
#df.loc[3, 'c'] = None
#df.loc[4, 'A'] = None
##print(df)
#print(df.info())
print(df.isnull())
print(df.isnull().sum())
#print(df.fillna(0))
#df2 = df.rename(columns={'A':'X','B':'Y','c':'Z'})
#print(df2)

#print(df.fillna(0,inplace=True))
#df['c'].fillna(df['c'].mean(),inplace=True)
#print(df)
print(df.sort_values(by='A',ascending=False))








