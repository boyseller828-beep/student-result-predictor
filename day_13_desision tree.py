from sklearn.tree import DecisionTreeClassifier
import numpy as np


#study hours
X = np.array([[1],[2],[3],[4],[5],[6]])

Y = np.array([0,0,0,1,1,1])

model = DecisionTreeClassifier()
model.fit(X,Y)

hours = float(input("Enter study hours :"))

pred = model.predict([[hours]])

print("Result :","pass" if pred[0]==1 else "Fail")

print('Accuracy :',model.score(X,Y))





































