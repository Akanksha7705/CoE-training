def display():
    while True:
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Balance")
        print("4. Exit")
        ch = int(input("Enter choice: "))
        match ch:
            case 1:
                deposit()
            case 2:
                withdraw()
            case 3:
                print("Balance: ", bal)
            case 4:
                print("Exit")
                break


def deposit():
    amount = int(input("Enter amount to be deposited: "))
    global bal
    if amount < 100:
        print("Amount should be more than 100")
    elif amount % 100 != 0:
        print("Re-Enter the valid amount")
    elif amount > 50000:
        print("Amount should not exceed 50k")
    else:
        print("Amount deposited successfully!!")
        bal += amount


def withdraw():
    amounts = int(input("Enter withdraw amount: "))
    global bal
    global trans
    if trans >= 3:
        print("Transaction limit reached")
        return
    if amounts < 100:
        print("Amount should be more than 100")
    elif amounts % 100 != 0:
        print("Re-Enter the valid amount")
    elif amounts > bal:
        print("Insufficient Balance")
    elif bal - amounts < 500:
        print("Min Balance should be 500")
    elif amounts > 20000:
        print("Amount should not exceed 20k")
    else:
        print("Transaction successful")
        bal -= amounts
        print(trans)
        trans += 1


class Bank:
    def val(self):
        numb = 0000
        chance = 0
        global bal
        bal = 3000
        global trans
        trans = 0
        while chance < 4:
            pin = int(input("Enter pin number: "))
            if pin == numb:
                display()
                exit()
            else:
                chance += 1
                print("Incorrect PIN")

            if chance == 4:
                print("Acc Blocked")
                break


obj = Bank()
obj.val()
