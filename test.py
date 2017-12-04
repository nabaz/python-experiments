import unittest
from misc import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_balance_greater_than_zero(self):
        a = BankAccount()
        a.deposit(10)
        self.assertTrue(a.balance > 0)

if __name__ == '__main__':
    unittest.main()
