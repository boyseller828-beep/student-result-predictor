from sklearn.model_selection import train_test_split


from sklearn.linear_model import LogisticRegression
import numpy as np

x = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
y = np.array([0,0,0,1,1,1,1,1,1,1])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(x_train, y_train)


print("Accuracy", model.score(x_test, y_test))
hours = float(input("Enter Study Hours :"))
pred = model.predict([[hours]])
print("Result :","pass" if pred[0] ==1 else 'fail')






















