# import streamlit as st
#
# # Initialize session state variables
# if 'bal' not in st.session_state:
#     st.session_state.bal = 3000
# if 'trans' not in st.session_state:
#     st.session_state.trans = 0
#
#
# # Bank class
# class Bank:
#     def __init__(self):
#         self.numb = 0000  # Default pin number
#         self.chance = 0
#
#     # Function to display options
#     def display(self):
#         st.write("### Bank Menu")
#         st.write("1. Deposit")
#         st.write("2. Withdrawal")
#         st.write("3. Balance")
#         st.write("4. Exit")
#
#         ch = st.radio("Select an option", [1, 2, 3, 4], index=0)
#
#         if ch == 1:
#             self.deposit()
#         elif ch == 2:
#             self.withdraw()
#         elif ch == 3:
#             st.write("Balance: ", st.session_state.bal)
#         elif ch == 4:
#             st.write("Exit")
#             st.stop()
#
#     # Deposit function
#     def deposit(self):
#         amount = st.number_input("Enter amount to be deposited:", min_value=100, step=100, format="%d")
#
#         if amount:
#             if amount < 100:
#                 st.error("Amount should be more than 100")
#             elif amount % 100 != 0:
#                 st.error("Re-Enter the valid amount")
#             elif amount > 50000:
#                 st.error("Amount should not exceed 50k")
#             else:
#                 st.success("Amount deposited successfully!!")
#                 st.session_state.bal += amount
#
#     # Withdraw function
#     def withdraw(self):
#         amount = st.number_input("Enter withdraw amount:", min_value=100, step=100, format="%d")
#
#         if amount:
#             if st.session_state.trans >= 3:
#                 st.error("Transaction limit reached")
#                 return
#
#             if amount < 100:
#                 st.error("Amount should be more than 100")
#             elif amount % 100 != 0:
#                 st.error("Re-Enter the valid amount")
#             elif amount > st.session_state.bal:
#                 st.error("Insufficient Balance")
#             elif st.session_state.bal - amount < 500:
#                 st.error("Min Balance should be 500")
#             elif amount > 20000:
#                 st.error("Amount should not exceed 20k")
#             else:
#                 st.success("Transaction successful")
#                 st.session_state.bal -= amount
#                 st.session_state.trans += 1
#
#     # PIN validation
#     def val(self):
#         pin = st.text_input("Enter PIN", type="password")
#         while self.chance < 4:
#             if pin:
#                 if int(pin) == self.numb:
#                     self.display()
#                 else:
#                     self.chance += 1
#                     st.error(f"Incorrect PIN. Attempts left: {4 - self.chance}")
#
#                 if self.chance == 4:
#                     st.error("Account Blocked")
#                     st.stop()
#
#
# # Main function to start the app
# def main():
#     st.title("Welcome to the Bank")
#     bank_obj = Bank()  # Create an instance of the Bank class
#     bank_obj.val()  # Call the val() method on the instance
#
#
# # Run the Streamlit app
# if __name__ == "__main__":
#     main()

import streamlit as st

# Initialize the balance variable
if 'balance' not in st.session_state:
    st.session_state.balance = 0.0


# Function to deposit money
def deposit(amount):
    st.session_state.balance += amount
    st.success(f"Deposited ${amount:.2f}. Current balance: ${st.session_state.balance:.2f}")


# Function to withdraw money
def withdraw(amount):
    if amount <= st.session_state.balance:
        st.session_state.balance -= amount
        st.success(f"Withdrew ${amount:.2f}. Current balance: ${st.session_state.balance:.2f}")
    else:
        st.error("Insufficient balance for this withdrawal.")


# Function to check balance
def check_balance():
    st.write(f"Current balance: ${st.session_state.balance:.2f}")


# Streamlit app UI
st.title("Bank Application")

# Menu options
menu = ["Deposit", "Withdraw", "Balance", "Exit"]
choice = st.sidebar.selectbox("Choose an option", menu)

if choice == "Deposit":
    amount = st.number_input("Enter amount to deposit", min_value=0.0, format="%.2f")
    if st.button("Deposit"):
        deposit(amount)

elif choice == "Withdraw":
    amount = st.number_input("Enter amount to withdraw", min_value=0.0, format="%.2f")
    if st.button("Withdraw"):
        withdraw(amount)

elif choice == "Balance":
    check_balance()

elif choice == "Exit":
    st.write("Thank you for using the bank application!")
    st.stop()

