import streamlit as stream
stream.title("CALCULATE GROSS SALARY")
sal = stream.number_input("Enter basic salary: ", min_value=1, step=1)
if stream.button("calculate"):
    hra = 0
    da = 0
    if sal < 10000:
        hra = (67 / sal) * 100
        da = (73 / sal) * 100
    elif sal < 20000:
        hra = (69 / sal) * 100
        da = (76 / sal) * 100
    else:
        hra = (73 / sal) * 100
        da = (89 / sal) * 100
    gs = hra + da + sal  # Calculate the gross salary
    total = round(gs, 2)  # round off the values upto two decimal
    stream.write(":red[Gross salary: ] ", total)
