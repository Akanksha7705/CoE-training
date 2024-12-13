import streamlit as st
st.title("Student Grade")
project = st.number_input("Project marks", min_value=0)
internal = st.number_input("Internal marks", min_value=0)
external = st.number_input("External marks", min_value=0)

if st.button("Grade"):

    if project >= 50 and internal >= 50 and external >= 50:
        pro = (70/100) * project
        inter = (10/100) * internal
        ext = (20/100) * external
        res = pro+inter+ext
        st.write("Total percentage:", res)
        if res > 90:
            st.write("Grade is A")
        elif res > 80:
            st.write("Grade is B")
        else:
            st.write("Grade is C")
    elif internal < 50:
        st.write("Failed in internal")
    elif external < 50:
        st.write("Failed in external")
    else:
        st.write("Failed in project")
