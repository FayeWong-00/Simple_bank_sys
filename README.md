
# Requirements
- Python 3.x
- No external dependencies required.

# Getting Started

## 1. Clone the repository (if necessary)
```sh
git clone <repository_url>
```
## 2. Run the banking system
```sh
python bank_sys.py
```

## 3. Customize and Test
You can modify and test the system by adding more test cases in the banking_system.py script or by update the custom_test.py script that uses the BankingSystem class. In custom_test.py it's already provided the following example:
```
from banking_system import BankingSystem

# Initialize a new banking system
bank = BankingSystem("accounts.csv", "transaction_log.csv")

# Create accounts
acc1 = bank.create_account("Alice", 100)
acc2 = bank.create_account("Bob", 200)

# Perform transactions
bank.deposit(acc1.account_id, 50)
bank.withdraw(acc2.account_id, 30)
bank.transfer(acc1.account_id, acc2.account_id, 70)

# Print updated balances
print("Updated Account Balances:")
for acc in bank.get_all_accounts():
    print(acc)

# The transaction log is recorded in 'transaction_log.csv'
```



## Methods
### create_account(name: str, starting_balance: float) -> BankAccount
```
Description: Creates a new bank account with a given name and starting balance.

Parameters:

name (str): The name of the account holder.

starting_balance (float): The initial balance of the account (default is 0.0).

Returns: A BankAccount object representing the newly created account.
```

### deposit(account_id: int, amount: float) -> float
```
Description: Deposits a specified amount into the account.

Parameters:

account_id (int): The ID of the account to deposit money into.

amount (float): The amount to deposit.

Returns: The updated balance of the account.
```


### withdraw(account_id: int, amount: float) -> float
```
Description: Withdraws a specified amount from the account.

Parameters:

account_id (int): The ID of the account to withdraw money from.

amount (float): The amount to withdraw.

Returns: The updated balance of the account.
```

### transfer(from_id: int, to_id: int, amount: float)
```
Description: Transfers a specified amount from one account to another.

Parameters:

from_id (int): The ID of the account to transfer money from.

to_id (int): The ID of the account to transfer money to.

amount (float): The amount to transfer.

Returns: None. The balances of both accounts are updated, and the transaction is logged.
```

### get_all_accounts() -> List[Dict]
```
Description: Retrieves all accounts in the system.

Returns: A list of dictionaries representing all accounts. Each dictionary contains account_id, name, and balance.
```

