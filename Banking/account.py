class BankAccount: 

    account_acounter=1000

    def __init__(self,name,balance=0):
        self.account_number=BankAccount.account_acounter
        BankAccount.account_acounter +=1
        self.name=name
        self.__balance=balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance+=amount
            print(f"Deposit of {amount} successfull.New balance: {self.__balance}")
        else:
            print("Withdrawal amount must be positive. ")

    def withdraw(self,amount):
        if amount>0:
            if(amount<=self.__balance):
                self.__balance-=amount
                print(f"Withdrawl of {amount} successfull. New balance:{self.__balance}")
        else:
            print("Withdrawl amount must be positive: ")
    
    def display_balance(self):
        print(f"AccountNo. : {self.account_acounter} , Account Holder : {self.name} , Balance : {self.__balance}")

class SavingAccount(BankAccount):
    def __init__(self, name, balance=0 , interest_rate=0.5):
        super().__init__(name, balance)
        self.interest_rate=interest_rate
    
    def calculate_interest(self):
        months=int(input("How many months to calculate the interest. "))
        interest =  self.interest_rate * months * self.get_balance()
        self.deposit(interest)
        print(f"Interest applied: {interest}. New Balance: {self.get_balance()}")


class CurrrentAccount(BankAccount):
    def __init__(self, name, balance=0, overdraft_limit=100000):
        super().__init__(name, balance)
        self.overdraft_limit=overdraft_limit