from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
x  = np.array ([0,1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
y = np.array ([35,40,45,50,55,70,75,80,85,90,95])
model = LinearRegression()
model.fit(x, y)
print('Coefficient (slope):', model.coef_[0])
print('Intercept:', model.intercept_)
years_of_experience = 11
predicted_salary = model.predict(np.array([[years_of_experience]]))

print(f"Predicted salary for {years_of_experience} years of experience: ${predicted_salary[0]*1000:.2f}")

plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, model.predict(x), color='red', label='Regression line')
plt.scatter([[years_of_experience]],predicted_salary,color = 'green', label = f'prediction {years_of_experience}yrs'),
plt.xlabel('Years of Experience')
plt.ylabel('Salary($1000)')
plt.title('simple linear regression:Salary vs Experience')
plt.legend()
plt.show()



















