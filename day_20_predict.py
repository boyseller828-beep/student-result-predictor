import pickle
import pandas as pd

# load model
model = pickle.load(open("model_2.pkl","rb"))


# input
math = float(input("Enter your Math marks :"))

science = float(input("Enter your Science marks :"))




data = pd.DataFrame([[math,science]],columns=["Math","Science"])
#prediction

pred = model.predict(data)

if pred[0]==1:
    print("Pass")
else:
    print("Fail")    

































