from sklearn.linear_model import LogisticRegression
import numpy as np
#study hours
x = np.array([[1],[2],[3],[4],[5],[6]])
#result(0 = fail,1= pass)
y = np.array([0,0,0,1,1,1])

model = LogisticRegression()
model.fit(x,y)
#prediction
hours = float(input("Enter Study Hours :"))
pred = model.predict([[hours]])
if pred[0] == 1:
    print('pass')
else:
    print('fail')   
print("Accuracy :",model.score(x,y)) 









