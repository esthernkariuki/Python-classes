class Account:
    def __init__(self,name,number):
        self.name=name
        self.number=number
        self.balance=0
        self.deposits=[]
        self.withdraws=[]
        self.is_frozen=False
        self.minimum_balance=0


# Deposit: method to deposit funds, store the deposit and return a message with the new balance to the customer. It should only accept positive amounts.

    def deposit(self,amount):
        if amount<=0:
            return f"{self.name} your deposit is must be positive number"
        self.balance += amount
        self.deposits.append(amount)
        return f"Hello {self.name} you have deposited {amount} your balance is {self.balance}"
        

# Withdraw: method to withdraw funds, store the withdrawal and return a message with the new balance to the customer. An account cannot be overdrawn.
    def withdraw_amount(self,amount):
        if amount<=0:
            return f"{self.name} your balance is negative number"
        if amount > self.balance:
            return f"{self.name} have insufficient balance.Your balance is {self.balance} top up your account and try again"
        self.balance -= amount
        self.withdraws.append(amount)
        return f"Hello {self.name} you have withdrawn {amount} your balance is {self.balance}"

# Transfer Funds: Method to transfer funds from one account to an instance of another account.

    def transfer_amount(self,amount):
        if amount<=0:
            return f"{self.name} your balance is negative number"
        if amount >self.balance:
            return f"{self.name} have insufficient balance.Your balance is {self.balance} top up your account and try again"
        self.balance-=amount
        self.withdraws.append(amount)
        return f" Confirmed {self.name} have successfull send {amount} to {self.number} your new balance is {self.balance}"


# Get Balance: Method to calculate an account balance from deposits and withdrawals.
    def get_balance(self):
        return f"Your account balance is {self.balance}"

# Request Loan: Method to request a loan amount.
    def request_loan(self,amount):
         if amount<=0:
            return f"{self.name} your balance is negative number"
         self.balance += amount
         return f"{self.name} you have received loan amount {amount},your new balance is {self.balance}"
    
# Repay Loan: Method to repay a loan with a given amount.
    def repay_loan(self,amount):
        if amount<=0:
             return f"{self.name} your balance is negative number"
        self.balance-=amount
        return f"{self.name} you have repayed {amount} your account balance is {self.balance}"
# View Account Details: Method to display the account owner's details and current balance.
    def view_account_details(self):
        return f"{self.name} your balance is {self.balance}"
             
# Change Account Owner: Method to update the account owner's name.
    def change_account_owner(self,new_name):
        self.name=new_name
        return f"Hello,{self.name}"
# Account Statement: Method to generate a statement of all transactions in an account. (Print using a for loop).
    def statement(self):
        print(f"Statement for {self.name}:")
        print("Deposits:")
        for deposit in self.deposits:
            print(f"{deposit}")
        print("Withdrawals:")
        for withdraw in self.withdraws:
            print(f"{withdraw}")
# Interest Calculation: Method to calculate and apply an interest to the balance. Use 5% interest. 
    def interest_calculation(self):
        interest=self.balance *0.05
        self.balance+=interest
        return f"{self.name} your interest is {self.balance}"

# Freeze/Unfreeze Account: Methods to freeze and unfreeze the account for security reasons.
    def freeze(self):
        self.is_frozen=True
        return f"{self.name} account and can't deposit or withdraw"
    
    def unfreeze(self):
        self.is_frozen=False
        return f"{self.name} account is unfrozen you can now deposit or withdraw"


# Set Minimum Balance: Method to enforce a minimum balance requirement. You cannot withdraw if your balance is less than this amount
    def minimum_balance(self,amount):    
        if amount < 0:
            return "Minimum balance cannot be negative."
        self.minimum_balance = amount
        return f"Minimum balance set to {self.minimum_balance}"
# Close Account: Method to close the account and set all balances to zero and empty all transactions
    def close_account(self):
        self.balance = 0
        self.deposits = []
        self.withdraws = []
        return f"{self.name} your account has been closed."
