import pandas as pd
import warnings


warnings.filterwarnings("ignore")

df = pd.read_csv("titanic.csv")

df['Age'] = df["Age"].fillna(df["Age"].mean())

df["Sex"] = df["Sex"].map({"male":0,"female":1})
x = df[["Pclass","Sex","Age","Fare"]]
y = df["Survived"]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train,y_train)
print("Accuracy: ",model.score(x_test,y_test))
Pclass = int(input("Class(1-3): "))
Sex = int(input("Enter Sex (0 for male, 1 for female): "))
Age = float(input("Enter Age: "))
Fare = float(input("Enter Fare: "))
prediction = model.predict([[Pclass,Sex,Age,Fare]])
print("Survived" if prediction[0] == 1 else "Not Survived")

import pickle
#save model
with open("titanic_model.pkl","wb") as f:
    pickle.dump(model,f)
print("Model saved as titanic_model.pkl")

with open("titanic_model.pkl","rb") as f:
    model = pickle.load(f)
print("model loaded")


model.prediction()





















