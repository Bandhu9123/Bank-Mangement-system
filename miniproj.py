accounts = {}

def create_account():
    name = input("Enter your name: ")
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        print("Account already exists!")
    else:
        accounts[acc_no] = {"name": name, "balance": 0}
        print("Account created successfully!")

def deposit():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_no]["balance"] += amount
        print("Amount deposited successfully!")
    else:
        print("Account not found!")

def withdraw():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if accounts[acc_no]["balance"] >= amount:
            accounts[acc_no]["balance"] -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")
    else:
        print("Account not found!")

def check_balance():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        print("Balance:", accounts[acc_no]["balance"])
    else:
        print("Account not found!")

while True:
    print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        create_account()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        check_balance()
    elif choice == '5':
        print("Thank you!")
        break
    else:
        print("Invalid choice!")