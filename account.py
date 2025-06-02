from datetime import datetime

class Transaction:
    def __init__(self, narration, amount, transaction_type):
        self.date_time = datetime.now()
        self.narration = narration
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.date_time.strftime('%Y-%m-%d %H:%M:%S')} {self.transaction_type.capitalize()}  {self.narration}  {self.amount:.2f}"

class Account:
    def __init__(self, owner, account_number):
        self.__owner = owner
        self.__account_number = account_number
        self.__transactions = []
        self.__is_frozen = False
        self.__minimum_balance = 0
        self.__loan_amount = 0.0

    def deposit(self, amount, narration="Deposit"):
        if self.__is_frozen:
            return "Account is frozen. Cannot deposit any amount."
        elif amount <= 0:
            return "Deposit amount must be positive."
        else:
            self.__transactions.append(Transaction(narration, amount, "deposit"))
            return f"Deposit successful. New balance: {self.get_balance():.2f}"

    def withdraw(self, amount, narration="Withdrawal"):
        if self.__is_frozen:
            return "Account is frozen. Cannot withdraw any amount."
        elif amount <= 0:
            return "Withdrawal amount must be positive."
        elif self.get_balance() - amount < self.__minimum_balance:
            return f"Insufficient funds or below minimum balance ({self.__minimum_balance:.2f})."
        else:
            self.__transactions.append(Transaction(narration, amount, "withdrawal"))
            return f"Withdrawal successful. New balance: {self.get_balance():.2f}"

    def transfer(self, target_account, amount, narration="Transfer"):
        if self.__is_frozen:
            return "Account is frozen. Cannot transfer any amount."
        elif amount <= 0:
            return "Transfer amount must be positive."
        elif self.get_balance() - amount < self.__minimum_balance:
            return f"Insufficient funds or below minimum balance ({self.__minimum_balance:.2f})."
        else:
            self.__transactions.append(Transaction(narration, amount, "transfer out"))
            target_account.deposit(amount, f"Transfer from {self.__account_number}")
            return f"Transfer successful. New balance: {self.get_balance():.2f}"

    def get_balance(self):
        balance = 0.0
        for transaction in self.__transactions:
            balance += transaction.amount
        return balance

    def request_loan(self, amount):
        if self.__is_frozen:
            return "Account is frozen. Cannot request loan."
        elif amount <= 0:
            return "Loan amount must be positive."
        else:
            self.__loan_amount += amount
            self.__transactions.append(Transaction("Loan granted", amount, "loan"))
            return f"Loan of {amount:.2f} granted. Outstanding loan: {self.__loan_amount:.2f}"

    def repay_loan(self, amount):
        if self.__is_frozen:
            return "Account is frozen. Cannot repay loan."
        elif amount <= 0:
            return "Repayment amount must be positive."
        elif self.__loan_amount == 0:
            return "No outstanding loan."
        else:
            repay_amount = min(amount, self.__loan_amount)
            self.__loan_amount -= repay_amount
            self.__transactions.append(Transaction("Loan repayment", repay_amount, "loan_repayment"))
            return f"Loan repaid: {repay_amount:.2f}. Remaining loan: {self.__loan_amount:.2f}"

    def view_account_details(self):
        return (f"Owner: {self.__owner}\n"
                f"Account number: {self.__account_number}\n"
                f"Balance: {self.get_balance():.2f}\n"
                f"Minimum balance: {self.__minimum_balance:.2f}\n"
                f"Outstanding loan: {self.__loan_amount:.2f}\n"
                f"Status: {'Frozen' if self.__is_frozen else 'Active'}")

    def change_account_owner(self, new_owner):
        self.__owner = new_owner
        return f"Account owner changed to {self.__owner}"

    def account_statement(self):
        print(f"Statement for {self.__owner} ({self.__account_number}):")
        for t in self.__transactions:
            print(t)
        print(f"Current balance: {self.get_balance():.2f}")

    def interest_calculation(self, rate=0.05):
        if self.__is_frozen:
            return "Account is frozen. Cannot apply interest."
        elif self.get_balance() > 0:
            interest = self.get_balance() * rate
            self.__transactions.append(Transaction("Interest", interest, "interest"))
            return f"Interest of {interest:.2f} applied. New balance: {self.get_balance():.2f}"
        else:
            return "No positive balance to apply interest."

    def freeze_account(self):
        self.__is_frozen = True
        return "Account frozen."

    def unfreeze_account(self):
        self.__is_frozen = False
        return "Account unfrozen."

    def set_minimum_balance(self, amount):
        if amount < 0:
            return "Minimum balance must be non-negative."
        else:
            self.__minimum_balance = amount
            return f"Minimum balance set to {self.__minimum_balance:.2f}"

    def close_account(self):
        if self.__is_frozen:
            return "Account is frozen. Unfreeze to close."
        else:
            self.__transactions.clear()
            self.__loan_amount = 0.0
            return f"{self.__owner}Account {self.__account_number} closed. All balances and transactions cleared."


if __name__ == "__main__":
    account1 = Account("Wamai", "08973")
    account2 = Account("Wanjiru", "42673")
    print(account1.deposit(1500))
    print(account2.deposit(500))
    print(account1.withdraw(300))
    print(account1.transfer(account2, 100))
    print(account1.request_loan(1200))
    print(account1.repay_loan(1000))
    print(account1.repay_loan(800))
    print(account1.view_account_details())
    account1.account_statement()
    print(account1.freeze_account())
    print(account1.deposit(200))
    print(account1.unfreeze_account())
    print(account1.deposit(200))
    print(account1.set_minimum_balance(50))
    print(account1.close_account())