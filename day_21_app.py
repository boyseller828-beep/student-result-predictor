import streamlit as st
import pandas as pd
import pickle
#load model
model = pickle.load(open("model_2.pkl","rb"))

st.title("Student Result Prediction")

#input

math = st.number_input("Enter your Math Marks :")
science = st.number_input("Enter your Science Marks :")

if st.button("Predict Result"):
    data = pd.DataFrame([[math,science]],columns=["Math","Science"])
    pred = model.predict(data)

    if pred[0]==1:
        st.success("Congratulations! You Passed.")
    else:
        st.error("Sorry! You Failed. Better luck next time.")





































