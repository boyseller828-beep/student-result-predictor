#Train Test model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
#Data
x = np.array([[1],[2],[3],[4],[5],[6]])
y = np.array([40,50,60,70,80,90])
#split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

#model
model = LinearRegression()
model.fit(x_train,y_train)
#test prediction
y_pred = model.predict(x_test)
print("Actual:",y_test)
print("predicted:",y_pred)
print("Accuracy",model.score(x_test,y_test))
    
        







































