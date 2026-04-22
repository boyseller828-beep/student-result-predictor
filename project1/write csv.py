import pandas as pd
dis ={
    'A':[1,2,3,4],"B" :[5,6,7,8],"c" :[9,10,11,12]
}
d = pd.DataFrame(dis)
print(d)
d.to_csv("my_Family1.csv",index=False)







