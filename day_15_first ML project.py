import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#load data

df = pd.read_csv("mark predictions.csv")
# input features
x = df[["Hours","Marks"]]

#output
y = df["result"]

#split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

#model
model = LogisticRegression()
model.fit(x_train,y_train)

#Accuracy

print("Accuracy",model.score(x_test,y_test))

#user input
Hours = float(input("Enter study hours :"))
marks = float(input("Enter previous marks :"))

pred = model.predict([[Hours,marks]])

if pred[0]==1:
    print("Result :Pass")
else:
    print("Result :Fail")








































