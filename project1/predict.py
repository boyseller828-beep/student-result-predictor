import pandas as pd
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

hours = float(input("Enter study hours : "))
marks = float(input("Enter previous marks : "))

# ✅ FIX: keep same feature names
input_data = pd.DataFrame([[hours, marks]], columns=["Hours", "Marks"])

result = model.predict(input_data)

print("Result:", "Pass" if result[0] == 1 else "Fail")




















