from bank_sys import BankingSystem

bank = BankingSystem("test_accounts.csv", "test_log.csv")

# Create accounts
acc1 = bank.create_account("John", 500)
acc2 = bank.create_account("Doe", 300)

# Perform transactions
bank.deposit(acc1.account_id, 100)
bank.withdraw(acc2.account_id, 50)
bank.transfer(acc1.account_id, acc2.account_id, 200)

# Print updated balances
print("Updated Account Balances:")
for acc in bank.get_all_accounts():
    print(acc)

print("\nTransaction log recorded in 'test_log.csv'")
