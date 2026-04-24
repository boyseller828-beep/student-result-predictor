import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import pickle

#load data
df = pd.read_csv("students.csv")

#features&target
x = df[["Math", "Science","English","Attendance"]]
y = df["Result"]

#split data
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

#pipeline
Pipeline = Pipeline([("imputer",SimpleImputer()),("scaler",StandardScaler()),("model",LogisticRegression())])
#train
Pipeline.fit(x_train,y_train)

#Accuracy
score = Pipeline.score(x_test,y_test)
print("Model Accuracy:", score)

#save model
with open("model_2.pkl","wb") as f:
    pickle.dump(Pipeline,f)
print("pipeline model saved as model_2.pkl")























