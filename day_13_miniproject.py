from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np
x = np.array([[1,40],
              [2,50],
              [3,55],
              [4,60],
              [5,70],
              [6,75],
              [7,80],
              [8,90],
              [9,95],
              [10,99]])


y = np.array([0,0,0,0,0,1,1,1,1,1])


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


model = DecisionTreeClassifier(max_depth=2)
model.fit(x_train, y_train)

print('Accuracy :', model.score(x_test, y_test))

hours = float(input("Enter study hours :"))
marks = float(input("Enter previous marks :"))

# Predict the outcome for the new data point
prediction = model.predict([[hours, marks]])
print("Result:", 'pass' if prediction[0] == 1 else 'fail')