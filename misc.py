# Check if a tree is a binary search tree
# design a bank account system using OOP
# Convert int to String representation
# OOP question to create classes for transactions, users, and accounts
# behavioral, job fit and case interview?
#difference between abstract class and interface.
#various questions about class path.
#Aspect oriented programming.
#difference between REST and SOAP  #


# design a bank account system using OOP
# http://anandology.com/python-practice-book/object_oriented_programming.html
class BankAccount():
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def overdrawn(self):
        return self.balance < 0

my_account = BankAccount()
my_account.withdraw(5)
print my_account.balance
print my_account.overdrawn()

class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print 'Sorry, minimum balance must be maintained.'
        else:
            BankAccount.withdraw(self, amount)
