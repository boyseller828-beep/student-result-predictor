from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle

df = pd.read_csv("students.csv")

x = df[["Math","Science","English","Attendance"]]

y = df["Result"]

params = {
    'C': [0.1, 1, 10]
}

gird = GridSearchCV(LogisticRegression(),params,cv=2)
gird.fit(x,y)



print ("Best params : ",gird.best_params_)
print("Best score : ",gird.best_score_)

best_model = gird.best_estimator_
pickle.dump(best_model,open("model_2.pkl","wb"))

print("Best model saved ✅")









































