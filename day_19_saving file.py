import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
#data load

df = pd.read_csv("mark predictions.csv")

x = df[["Hours","Marks"]]

y = df["result"]

# train

model = LogisticRegression()
model.fit(x,y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
























