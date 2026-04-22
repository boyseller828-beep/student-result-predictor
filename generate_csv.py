import pandas as pd
dis ={
    'Hours': [1,2,3,4,5,6,7,8],'Marks' :[40,50,55,60,70,80,85,90],'result' : [0,0,0,1,1,1,1,1]
}
d = pd.DataFrame(dis)
print(d)
d.to_csv("mark predictions.csv",index=False)
