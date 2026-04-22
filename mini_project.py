from sklearn.linear_model import LinearRegression
import numpy as np
# hours studied
x = np.array([[1], [2], [3], [4], [5],[6],[7],[8],[9],[10]])

# marks
y = np.array([10,20,30,40,50,60,70,80,90,100])
model = LinearRegression()
model.fit(x, y)
hours=float(input('enter study hours :'))
predicted_marks = model.predict([[hours]])
print('expected marks:', predicted_marks[0])
print("slope:",model.coef_)
print("intercept:",model.intercept_)





















