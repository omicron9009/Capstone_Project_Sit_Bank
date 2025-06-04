from Banking.account import SavingAccount , CurrrentAccount
from Banking.transactions import deposit , withdraw

accounts={}

def create_account():
    name = input("Enter your name : ").strip()
    account_type=input("Enter your account type (savings/current): ").strip().lower()
    initital_deposit = float(input("Enter initial deposit amount: "))
    if account_type =="savings":
        acc = SavingAccount(name,initital_deposit)
    elif account_type=="current":
        acc = CurrrentAccount(name,initital_deposit)
    else:
        print("Invalid account type . Please Choose savings or current")
    account_type[acc.account_number]= acc
    print(f"Accout created succesfully . Account Number : {acc.account_number}")

def login():
    account_number = int(input("Enter acount number :"))
    if account_number in accounts :
        user_acc= accounts[account_number]
        print(f"Welcome {user_acc.name} !")
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            if isinstance(user_acc,SavingAccount):
                print("4. Apply interest")
            print("5. Logut")

            choice=input("Choose an option : ")
            if choice=='1':
                amount=float(input("Enter amount to deposit: "))
                deposit(user_acc,amount)
            elif choice=='2':
                amount = float(input("Enter amount to withdraw: "))
                withdraw(user_acc,amount)
            elif choice=='3':
                print(f"Current balance: {user_acc.get_balance()}")
            elif choice=='4' and isinstance(user_acc,SavingAccount):
                user_acc.calculate_interest()
            elif choice=='5':
                print("Logging out...")
                break
            else:
                print("Invalid Choice..")
    else:
        print("Acount not found .. Create an Account first ")
    
def main():
    print("Welcome to the Sit Bank !".center(50))
    print("Nagpur SIT branch ".center(50))

    while True:
        print("\n1. Create Account: ")
        print("2. Login")
        print("3. Exit")
        choice=input("Choose an option ...")
        if choice=='1':
            create_account()
        elif choice=='2':
            login()
        elif choice=='3':
            print("Thank you for using Sit Bank . good Bye!")
            break
        else:
            print("Invalid choice . Pleae Enter a valid option ")
if __name__ == "__main__":
    main()
 












