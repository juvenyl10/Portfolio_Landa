
class Account:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            if amount % 100 == 0:
                self.balance += amount
                return "Deposit Successful."
            else:
                return "Error: Deposit amount must be divisible by 100."
        else:
            return "Error: Cannot deposit negative amount."

    def withdraw(self, amount):
        if amount > 0 and amount % 100 == 0:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
        else:
            return "Error: Withdrawal amount must be divisible by 100."

    def check_balance(self):
        print(f"Current balance: {self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, interest_rate):
        super().__init__(account_number)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        return interest


class Bank:
    def __init__(self):
        self.accounts = {}
        self.maintainingBalance = {}

    def create_account(self, account_number, initial_balance):
        if account_number not in self.accounts:
            if initial_balance >= 1000 and initial_balance % 100 == 0:
                account = Account(account_number)
                account.balance = initial_balance
                self.accounts[account_number] = account
                return "Account Created Successfully!"
            else:
                return "Error: Initial balance should be at least 1000 and divisible by 100."
        else:
            return "Error: Account number already exists."

    def create_savings_account(self, account_number, interest_rate, amt, mbal):
        if account_number not in self.accounts:
            if amt >= 0:
                savings_account = SavingsAccount(account_number, interest_rate)
                savings_account.deposit(amt)
                self.accounts[account_number] = savings_account
                self.maintainingBalance[account_number] = mbal
                print(f"Savings account {account_number} created successfully")
            else:
                input("Balance cannot be negative")
        else:
            print("Account number already exist")

    def close_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            return "Account Closed Successfully!"
        else:
            return "Error: Account not found."

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].deposit(amount)
        else:
            return "Error: Account not found."

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].withdraw(amount)
        else:
            return "Error: Account not found."

    def check_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].check_balance()
        else:
            return "Error: Account not found."

    def calculate_interest(self, account_number):
        if account_number in self.accounts:
            if isinstance(self.accounts[account_number], SavingsAccount):
                return self.accounts[account_number].calculate_interest()
            else:
                return "Error: Not a savings account."
        else:
            return "Error: Account not found."

    def check_Account(self):
        return self.accounts

    def check_balance(self, account_number):
        if account_number in self.accounts:
            self.accounts[account_number].check_balance()
        else:
            input("Account number does not exist | Create account first!")


bank = Bank()
while True:
    print("\t\t\t\t\tBANKING SYSTEM\t\t\t\t\t")
    print("--------------------------------------------------------")
    print("[1] - Deposit\n[2] - Withdraw\n[3] - Create Account\n[4] - Create Savings Account\n[5] - Calculate Interest")
    print("[6] - Close Account\n[7] - View Account\n[X] - Exit")
    choice = input("Enter Choice: ")

    if choice == "1":
        if bank.check_Account():
            accountN = input("Enter Account Number: ")
            amt = int(input("Enter Amount: "))
            bank.deposit(accountN, amt)
            input("Success! | Press any key to continue")

        else:
            input("Error! Create account first! | Press any key to continue")

    elif choice == "2":
        if bank.check_Account():
            accountN = input("Enter Account Number: ")
            amt = int(input("Enter amount: "))
            bank.withdraw(accountN, amt)
            input("Success! | Press any key to continue")

        else:
            input("Error! Create Account first! | Press any key to continue")

    elif choice == "3":
        while True:
            accountN = input("Enter account Number: ")
            if len(accountN) != 9:
                input("Error! Account number must be 9 digits | Press any key to continue")
            else:
                bal = int(input("Enter Initial Balance: "))
                bank.create_account(accountN, bal)
                input("Success! | Press any key to continue")
                break

    elif choice == "4":
        while True:
            accountN = input("Enter Account Number: ")
            if accountN in Account.get_account_number():
                input("Enter different account number! | Press any key to continue")
            else:
                if len(accountN) !=9:
                    input("Error! Account number must be 9 digits! | Press any key to continue")

                else:
                    while True:
                        acc = input("Enter account number: ")
                        if acc in Account.get_account_number():
                            input("Please Enter different account number")
                        elif len(acc) != 9:
                            input("Please enter 9 characters for account number")
                        else:
                            amt = int(input("Enter initial amount: "))
                            r = int(input("Enter Interest rate: "))
                            bal = int(input("Enter maintaining balance: "))
                            bank.create_savings_account(acc, r, amt, bal)
                            input("Success! Press any key to continue ")
                            break

    elif choice == "5":
        if bank.check_Account():
            accountN = input("Enter account Number: ")
            bank.calculate_interest(accountN)
            input("Press any key to continue")

        else:
            input("Error! Create Account first! | Press any key to continue")

    elif choice == "6":
        if bank.check_Account():
            accountN = input("Enter account Number: ")
            if accountN not in bank.check_Account():
                input("account number does not exist | Press any key to continue")

            else:
                bank.close_account(accountN)
                input("Success! | Press any key to continue")

        else:
            input("Error! Create account first! | Press any key to continue")

    elif choice == "7":
        if bank.check_Account():
            accountN = input("Enter account Number: ")
            bank.check_balance(accountN)
            input("Press any key to continue")

        else:
            input("Error! Create account first! | Press any key to continue")

    elif choice.upper() == "X":
        input("Thank you! | Press any key to continue")
        break

    else:
        input("Invalid input! | Press any key to continue")






