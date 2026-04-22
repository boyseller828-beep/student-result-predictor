import pandas as pd
# create a dataframe
monthly_premiums = [10,20,30,50,40,60]
months = ['jan','feb','mar','apr','may','jun']
monthly_premiums_series = pd.Series(monthly_premiums, index=months)
print(monthly_premiums_series)






