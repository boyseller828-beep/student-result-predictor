
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
df = pd.read_csv("mark predictions.csv")
x = df[["Hours","Marks"]]
y = df["result"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)



model = LogisticRegression(C=0.5)
model.fit(x_train,y_train)

print("Accuracy :",model.score(x_test,y_test))

hours = float(input("Enter study hours :"))

marks = float(input("Enter previous marks :"))
user_data = pd.DataFrame([[hours,marks]],columns=["Hours","Marks"])
user_data = scaler.transform(user_data)
pred = model.predict(user_data)

print("Result:","pass"if pred[0] ==1 else "Fail")
 





























