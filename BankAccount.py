class BankAccount:
    def __init__(self, owner, balance):
        self.data = {
            "owner": owner,
            "balance": balance,
            "history": []
            }

    def deposit( self,amount):
        # self.amount: amount
        self.data["balance"] += amount
        print(f"Deposited ${amount}. New Balance: ${self.data['balance']}")
        self.data['history'].append(f"Deposited ${amount}")

    def withdraw(self,amount):
        if amount > self.data["balance"]:
            print(f"Insufficient funds! you on;y have ${self.data['balance']}")
        else:
            self.data['balance'] -= amount
            print(f"Withdraw ${amount}. Remaining balance: ${self.data['balance']}")
            self.data["history"].append(f"Withdrawn ${amount}")

    def print_statment(self):
        print("---STATMENT---")
        for transaction in self.data["history"]:
            print(transaction)
        print("--------------")


class SavingAccount(BankAccount):
    def __init__(self, owner, balance,interest_rate):
        super().__init__(owner, balance)
        self.data["interest_rate"] = interest_rate

    def add_intrest(self):
        interest = self.data["balance"] * self.data["interest_rate"]
        self.data["balance"] += interest
        self.data["history"].append(f"Interest added of amount ${interest}")



Account = SavingAccount("ShreyashBhai",3000,3)

Account.deposit(100)
Account.withdraw(2000)
Account.withdraw(2000)
Account.add_intrest()
Account.print_statment()
