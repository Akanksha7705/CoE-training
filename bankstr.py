import streamlit as st

st.title("Bank")


def display():
    while True:
        st.write("1. Deposit")
        st.write("2. Withdrawal")
        st.write("3. Balance")
        st.write("4. Exit")
        ch = st.number_input("Enter choice: ", min_value=0, key="choice")
        # ch = st.radio("Select an option", [1, 2, 3, 4], key="option")
        # match ch:
        #     case 1:
        #         deposit()
        #     case 2:
        #         withdraw()
        #     case 3:
        #         st.write("Balance: ", bal)
        #     case 4:
        #         st.write("Exit")
        #         break
        if ch == 1:
            deposit()
        elif ch == 2:
            withdraw()
        elif ch == 3:
            st.write("Balance: ", bal)
        elif ch == 4:
            st.write("Exit")
            st.stop()


def deposit():
    amount = st.number_input("Enter deposit amount: ", key="deposit")
    global bal
    if amount < 100:
        st.write("Amount should be more than 100")
    elif amount % 100 != 0:
        st.write("Re-Enter the valid amount")
    elif amount > 50000:
        st.write("Amount should not exceed 50k")
    else:
        st.write("Amount deposited successfully!!")
        bal += amount


def withdraw():
    amounts = st.number_input("Enter withdraw amount: ", key="withdraw")
    global bal
    global trans
    if trans >= 3:
        st.write("Transaction limit reached")
        return
    if amounts < 100:
        st.write("Amount should be more than 100")
    elif amounts % 100 != 0:
        st.write("Re-Enter the valid amount")
    elif amounts > bal:
        st.write("Insufficient Balance")
    elif bal - amounts < 500:
        st.write("Min Balance should be 500")
    elif amounts > 20000:
        st.write("Amount should not exceed 20k")
    else:
        st.write("Transaction successful")
        bal -= amounts

        trans += 1


def val():
    numb = 0000
    chance = 0
    global bal
    bal = 3000
    global trans
    trans = 0
    # while chance < 4:
    if chance > 4:
        st.write("Account blocked")
        st.stop()
    else:
        pin = st.number_input("Enter PIN", key="pin_input")
        if st.button("Continue"):
            if pin == numb:
                display()
                exit()
            else:
                chance += 1
                st.write("Incorrect PIN")

            if chance == 4:
                st.write("Acc Blocked")
            # break


def main():
    st.title("Welcome to the Bank")
    val()


# Run the Streamlit app
if __name__ == "__main__":
    main()
