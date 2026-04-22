import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

#load data
df = pd.read_csv("students.csv")

#features&target
x = df[["Math", "Science"]]
y = df["Result"]

#split data
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

#model
model = LogisticRegression()
model.fit(x_train, y_train)

#Accuracy
accuracy = model.score(x_test, y_test)

print("Model Accuracy:", accuracy)

#save model
pickle.dump(model,open("model_2.pkl","wb"))
print("Model saved ")    






















