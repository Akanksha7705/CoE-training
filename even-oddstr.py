import streamlit as st
st.title("Number identification")
a = st.number_input("Enter a number: ",min_value=1,step=1)
if st.button("Check"):
    if a % 2 == 0:
        st.success("Even ")
    else:
        st.error("Odd")

