from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
x = np.array([[2],[4],[6],[8],[10],[12]])
y = np.array([10,20,40,60,80,90])
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.5)
model = LinearRegression()
model.fit(x_train, y_train)

print("Accuracy :",model.score(x_test,y_test))
hours = float(input('Enter study hours :'))
print("predicted marks :",model.predict([[hours]])[0])
print('Train Data:',x_train)
print("Test data:",x_test)











































