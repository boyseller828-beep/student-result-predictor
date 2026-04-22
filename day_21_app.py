<<<<<<< HEAD
import streamlit as st
import pandas as pd
import pickle
#page config
st.set_page_config(page_title="Student mark predictor",page_icon= "📚",layout="centered")

st.title("Student Result Prediction App")
st.write("This app predicts whether a student will pass or fail based on their marks in Math and Science. Enter the marks and click the predict button to see the result.")




#load model
model = pickle.load(open("model_2.pkl","rb"))
#layout(side-by-side input and output)
col1, col2 = st.columns(2)

with col1:
    math = st.number_input("📖Enter your Math Marks :",min_value=0,max_value=100)

with col2:
    science = st.number_input("🧪Enter your Science Marks :",min_value=0,max_value=100)

if st.button("Predict Result"):
    data = pd.DataFrame([[math,science]],columns=["Math","Science"])
    pred = model.predict(data)

    if pred[0]==1:
        st.success("student will pass ✅")
    else:
        st.error("Sorry! student will fail ❌. Better luck next time.")


#footer
st.markdown("---")
st.caption("Created by [Ahmad Afnan]")


































=======
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





































>>>>>>> be272ab9125725b7fa626f7035ee2305e204d7fa
