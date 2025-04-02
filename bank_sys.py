import csv
import os
import datetime

class BankAccount:
    def __init__(self, account_id, name, balance=0.0):
        self.account_id = account_id
        self.name = name
        self.balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def to_dict(self):
        return {"account_id": self.account_id, "name": self.name, "balance": self.balance}


class BankingSystem:
    def __init__(self, accounts_file="bank_data.csv", log_file="transaction_log.csv"):
        self.accounts_file = accounts_file
        self.log_file = log_file
        self.accounts = {}
        self.load_accounts()

    def create_account(self, name, starting_balance=0.0):
        """Creates a new account and logs the creation."""
        account_id = len(self.accounts) + 1
        if name in [acc.name for acc in self.accounts.values()]:
            raise ValueError("Account with this name already exists.")
        new_account = BankAccount(account_id, name, starting_balance)
        self.accounts[account_id] = new_account
        self.save_accounts()
        self.log_transaction("CREATE", new_account.account_id, new_account.name, None, None, starting_balance, new_account.balance)
        return new_account

    def get_account(self, account_id):
        """Retrieves an account by its ID."""
        return self.accounts.get(account_id, None)

    def deposit(self, account_id, amount):
        """Deposits money into an account and logs the transaction."""
        account = self.get_account(account_id)
        if not account:
            raise ValueError("Account not found.")
        new_balance = account.deposit(amount)
        self.save_accounts()
        self.log_transaction("DEPOSIT", account.account_id, account.name, None, None, amount, new_balance)
        return new_balance

    def withdraw(self, account_id, amount):
        """Withdraws money from an account and logs the transaction."""
        account = self.get_account(account_id)
        if not account:
            raise ValueError("Account not found.")
        new_balance = account.withdraw(amount)
        self.save_accounts()
        self.log_transaction("WITHDRAW", account.account_id, account.name, None, None, amount, new_balance)
        return new_balance

    def transfer(self, from_id, to_id, amount):
        """Transfers money between accounts and logs the transaction."""
        if from_id == to_id:
            raise ValueError("Cannot transfer to the same account.")
        from_acc = self.get_account(from_id)
        to_acc = self.get_account(to_id)
        if not from_acc or not to_acc:
            raise ValueError("One or both accounts not found.")
        from_acc.withdraw(amount)
        to_acc.deposit(amount)
        self.save_accounts()
        self.log_transaction("TRANSFER", from_acc.account_id, from_acc.name, to_acc.account_id, to_acc.name, amount, from_acc.balance)

    def get_all_accounts(self):
        """Returns all accounts as a list of dictionaries."""
        return [acc.to_dict() for acc in self.accounts.values()]

    def save_accounts(self):
        """Saves all accounts to a CSV file."""
        with open(self.accounts_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["account_id", "name", "balance"])
            writer.writeheader()
            for acc in self.accounts.values():
                writer.writerow(acc.to_dict())

    def load_accounts(self):
        """Loads accounts from a CSV file if it exists."""
        if not os.path.exists(self.accounts_file):
            return
        with open(self.accounts_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                account = BankAccount(int(row["account_id"]), row["name"], float(row["balance"]))
                self.accounts[account.account_id] = account

    def log_transaction(self, action, account_id, account_name, target_id, target_name, amount, balance):
        """Logs a transaction to the transaction log CSV."""
        with open(self.log_file, "a", newline="") as f:
            writer = csv.writer(f)
            if os.stat(self.log_file).st_size == 0:
                writer.writerow(["timestamp", "action", "account_id", "account_name", "target_id", "target_name", "amount", "balance"])
            writer.writerow([datetime.datetime.now(), action, account_id, account_name, target_id if target_id else "", target_name if target_name else "", amount, balance])


# Example usage
if __name__ == "__main__":
    bank = BankingSystem()

    acc1 = bank.create_account("Alice", 100)
    acc2 = bank.create_account("Bob", 200)

    print(f"Created account: {acc1.to_dict()}")
    print(f"Created account: {acc2.to_dict()}")

    bank.deposit(acc1.account_id, 50)
    print(f"Alice's new balance: {acc1.balance}")

    bank.withdraw(acc2.account_id, 30)
    print(f"Bob's new balance: {acc2.balance}")

    bank.transfer(acc1.account_id, acc2.account_id, 70)
    print(f"Alice's new balance after transfer: {acc1.balance}")
    print(f"Bob's new balance after receiving transfer: {acc2.balance}")

    print("\nTransaction log saved in 'transaction_log.csv'")
