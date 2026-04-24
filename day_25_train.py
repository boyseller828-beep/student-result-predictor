from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import pickle
df = pd.read_csv("titanic.csv")
#fill missing values
df["Age"].fillna(df["Age"].mean(),inplace= True)
df["Fare"].fillna(df["Fare"].mean(),inplace=True)

#convert text to numbers

df["Sex"] = df["Sex"].map({"male": 0,"female":1})

x = df[["Pclass","Age","Fare","Sex",]]

y = df["Survived"]
#split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.5,random_state=42)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)



models ={
    "Log":LogisticRegression(),"KNN":KNeighborsClassifier(n_neighbors=3),"DTC":DecisionTreeClassifier(max_depth=10)
}

for name,model in models.items():
    model.fit(x_train,y_train)
    accuracy = model.score(x_test,y_test)
    print(name,"->Accuracy :",accuracy)
    
#choose KNN
from sklearn.neighbors import KNeighborsClassifier


model = KNeighborsClassifier(n_neighbors=5)
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model,x,y,cv=5)
print("Cross-validation score:",scores)
print("Average Accuracy :",scores.mean())

#train final model
model.fit(x_train,y_train)



#save model
pickle.dump(model,open("Knn_model.pkl","wb"))

print("Model saved")






















