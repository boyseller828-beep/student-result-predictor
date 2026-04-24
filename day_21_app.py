
import streamlit as st
import pandas as pd
import pickle
#page config
st.set_page_config(page_title="Student mark predictor",page_icon= "📚",layout="centered")

st.title("Student Result Prediction App")
st.write("This app predicts whether a student will pass or fail based on their marks in Math, Science,English,Attendance. Enter the marks and click the predict button to see the result.")




#load model
model = pickle.load(open("model_2.pkl","rb"))
#layout(side-by-side input and output)
#col1, col2, col3, col4 = st.columns(4)

#with col1:
math = st.number_input("📖Enter your Math Marks :",min_value=0,max_value=100)

#with col2:
science = st.number_input("🧪Enter your Science Marks :",min_value=0,max_value=100)

#with col3:
english = st.number_input("📚Enter your English Marks :",min_value=0,max_value=100)

#with col4:
attendance = st.number_input("👥Enter your Attendance :",min_value=0,max_value=100)

if st.button("Predict Result"):
    data = pd.DataFrame([[math,science,english,attendance]],columns=["Math","Science","English","Attendance"])
    pred = model.predict(data)

    if pred[0]==1:
        st.success("student will pass ✅")
    else:
        st.error("Sorry! student will fail ❌. Better luck next time.")
    prob = model.predict_proba(data)
    st.write(f"Probability of passing: {prob[0][1]*100:.2f}%")

#footer
st.markdown("---")
st.caption("Created by [Ahmad Afnan]")
































