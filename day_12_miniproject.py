from sklearn.neighbors import KNeighborsClassifier
import numpy as np

X = np.array([[1,50]
             ,[2,60]
             ,[3,70]
             ,[4,80]])
Y = np.array([0,0,1,1])

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X,Y)

print("Accuracy :",model.score(X,Y))

hours = float(input("enter study hours"))
score = float(input("enter score"))
pred = model.predict([[hours, score]])

if pred[0] ==1:
    print("pass")
else:
    print("fail")

































