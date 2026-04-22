from sklearn.neighbors import KNeighborsClassifier
import  numpy as np
#Study hours

X = np.array([[1],[2],[3],[4],[5],[6]])

Y = np.array([0,0,0,1,1,1])

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X,Y)
hours = float(input("enter study hours :"))
pred = model.predict([[hours]])
print("Result:","pass" if pred[0] == 1
      else 'fail')





































