import unittest
import os
from bank_sys import BankingSystem

class TestBankingSystem(unittest.TestCase):
    def setUp(self):
        """Set up a fresh bank instance with a test file"""
        self.bank = BankingSystem("test_bank_data.csv")

    def tearDown(self):
        """Remove the test file after each test"""
        if os.path.exists("test_bank_data.csv"):
            os.remove("test_bank_data.csv")

    def test_create_account(self):
        acc = self.bank.create_account("Alice", 100)
        self.assertEqual(acc.name, "Alice")
        self.assertEqual(acc.balance, 100)

    def test_deposit(self):
        acc = self.bank.create_account("Bob", 50)
        new_balance = self.bank.deposit(acc.account_id, 30)
        self.assertEqual(new_balance, 80)

    def test_withdraw(self):
        acc = self.bank.create_account("Charlie", 200)
        new_balance = self.bank.withdraw(acc.account_id, 50)
        self.assertEqual(new_balance, 150)

    def test_overdraft_prevention(self):
        acc = self.bank.create_account("David", 20)
        with self.assertRaises(ValueError):
            self.bank.withdraw(acc.account_id, 30)

    def test_transfer(self):
        acc1 = self.bank.create_account("Eve", 500)
        acc2 = self.bank.create_account("Frank", 100)
        self.bank.transfer(acc1.account_id, acc2.account_id, 200)
        self.assertEqual(acc1.balance, 300)
        self.assertEqual(acc2.balance, 300)

    def test_transfer_insufficient_funds(self):
        acc1 = self.bank.create_account("Grace", 50)
        acc2 = self.bank.create_account("Hank", 100)
        with self.assertRaises(ValueError):
            self.bank.transfer(acc1.account_id, acc2.account_id, 100)

if __name__ == "__main__":
    unittest.main()
