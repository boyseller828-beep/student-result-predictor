import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler

#load data

df = pd.read_csv("mark predictions.csv")

x = df[["Hours","Marks"]]

y = df["result"]



#split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.5,random_state=42)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

#models
models ={
    "LogisticRegression":LogisticRegression(),"KNN":KNeighborsClassifier(n_neighbors=2),"Decision Tree":DecisionTreeClassifier(max_depth=2)
}
#train +compare
for name,model in models.items():
    model.fit(x_train,y_train)
    accuracy = model.score(x_test,y_test)
    print(name,"->Accuracy: ",accuracy)




































