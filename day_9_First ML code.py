from sklearn.linear_model import LinearRegression
import numpy as np

# input (hours studied)
x = np.array([[1], [2], [3], [4], [5]])

# output marks
y = np.array([40, 50, 60, 70, 80])

model = LinearRegression()
model.fit(x, y)

# predict
prediction = model.predict([[6]])
print('predicted marks :', prediction)












