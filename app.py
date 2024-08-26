import streamlit as st

st.header('Calculator APP')
st.write('Web app created by Nithin')

num1 = st.number_input("Enter the first number",value=0)
option = st.selectbox(label="Select an operation",
             options=["+","-","*","/"])
num2 = st.number_input("Enter the second number",value=0)
btn = st.button("Calculate")

if btn:
    if option=="+":
        st.subheader(num1+num2)
    elif option=="-":
        st.subheader(num1-num2)
    elif option=="*":
        st.subheader(num1*num2)
    elif option=="/":
        st.subheader(num1/num2)